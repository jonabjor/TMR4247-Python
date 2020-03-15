import numpy as np
# Verdier fra tabell for skalering fra modell til fullskala
def holtrop_formfaktor(V_m, R_tm, V_s, ro_a, Cb, Cp, Ca, Lwl_m, B_m, T_m, ro_m, S_m, v_m, Cd_m, H_m
    , At_m, L_cb_m, displ_m, Lwl_s, B_s, ro_s, S_s, v_s, Cd_s, H_s
    , At_s, L_r):

    C_bdm = 0
    # Beregning av Reynoldstall til modell
    R_nm = (V_m * Lwl_m) / v_m 

    # Beregnig av Froudetallet
    F_n = V_m / np.sqrt(Lwl_m * 9.81)

    # Beregning av total motstandskoeffisient for modell (C_TM)
    C_tm = R_tm / (1/2 * ro_m * V_m**2 * S_m) 

    # Beregning av restmotstand
    C_fm = 0.075 / ((np.log10(R_nm) - 2)**2) # Friksjonsmotstandskoeffisient i modell
    k = 0.93 - 1 + 0.487118 * (B_m/Lwl_m)**(1.06806)*(T_m/Lwl_m)**(0.46106)*(Lwl_m / L_r)**(0.121563)*(Lwl_m**3/displ_m)**0.36486*(1-Cp)**(-0.604247) # Holtrop formfaktor
    C_vm = C_fm * (1+k) # Viskøs motstandskoeffisient
    C_aam = (ro_a * Cd_m * At_m) / (S_m * ro_m) # Luftmotstandskoeffisient
    C_rm = C_tm - C_vm - C_aam - C_bdm # Restmotstanden

    oppg_b_matrix_1 = np.array([V_m, R_tm, F_n, R_nm, C_tm, C_fm, C_vm, C_rm])
    oppg_b_matrix_1 = np.transpose(oppg_b_matrix_1)

    # Beregning av Reynoldstall skip
    R_ns = (V_s * Lwl_s) / v_s


    # Beregning av fullskala motstandskoeffisient
    C_fs = 0.075 / ((np.log10(R_ns) - 2)**2) # Friksjonsmotstandskoeffisient i fullskala
    Dcf = (110*np.power(H_s*V_s, 0.21) - 403) * C_fs**2 # Ruhetstillegg
    C_aas = (ro_a * Cd_s * At_s) / (S_s * ro_s) # Luftmotstandskoeffisient
    C_ts = C_rm + (1+k)*(C_fs+Dcf)+C_aas+Ca # Fullskala motstandskoeffisient

    # Total motstand
    R_ts = 1/2 * ro_s * V_s**2 * S_s * C_ts
    R_ts /= 1000 # Konvertering fra [N] til [kN]

    oppg_b_matrix_2 = np.array([V_s, R_ns, C_fs, Dcf, C_ts, R_ts])
    oppg_b_matrix_2 = np.transpose(oppg_b_matrix_2)

    return oppg_b_matrix_1, oppg_b_matrix_2

