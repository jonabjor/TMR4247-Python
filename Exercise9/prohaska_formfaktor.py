import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def prohaska_formfaktor(V_m, R_tm, Lwl_m, v_m, ro_m, S_m):

    # Beregner Froudetallet
    F_n = V_m / np.sqrt(Lwl_m * 9.81)

    # Beregner Reynoldstallet
    R_nm = (V_m * Lwl_m) / v_m 

    # Beregning av total motstandskoeffisient for modell (C_TM)
    C_tm = R_tm / (1/2 * ro_m * V_m**2 * S_m) 

    # Beregning av restmotstand
    C_fm = 0.075 / ((np.log10(R_nm) - 2)**2) # Friksjonsmotstandskoeffisient i modell

    best_r = 0
    best_k = 0
    for i in range(6): # Prøver med 1 <= n <= 8
        y = C_tm / C_fm
        x = F_n**(i+3) / C_fm
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        print("Korrelasjonskoeffisient:", r_value, "(1+k):", intercept, "n =", i+3)
        if (r_value > best_r):
            best_r = r_value
            best_k = intercept - 1
    return best_k