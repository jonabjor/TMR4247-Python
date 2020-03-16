from setup import get_holtrop_param, get_hollenbach_param, get_sintef_formfaktor_param, get_holtrop_formfaktor_param, get_prohaska_formfaktor_param
from Holtrop import holtrop
from Hollenbach import hollenbach
from sintef_formfaktor import sintef_formfaktor
from holtrop_formfaktor import holtrop_formfaktor
from prohaska_formfaktor import prohaska_formfaktor
from tabulate import tabulate
import matplotlib.pyplot as plt

def main():
    # Henter inn Holtrop parametere og kaller på holtrop funksjonen
    holtrop_param = get_holtrop_param()
    holtrop_result = holtrop(*holtrop_param)

    # Henter inn Hollenbach parametere og kaller på holtrop funksjonen
    hollenbach_param = get_hollenbach_param()
    hollenbach_result = hollenbach(*hollenbach_param)

    # Henter inn Sintef Ocean formfaktor parametere og beregner motstand
    sintef_formfaktor_param = get_sintef_formfaktor_param()
    matrise1_sintef, matrise2_sintef, sintef_factor = sintef_formfaktor(*sintef_formfaktor_param)

    # Utskrift av resultater fra Sintef Ocean analyse
    print(tabulate(matrise1_sintef, headers=["Fart [m/s]", "Motstand [N]", "F_N" ,"Reynoldstall", "C_TM", 
    "C_FM", "C_VM", "C_RM"]))
    print("\n")
    print(tabulate(matrise2_sintef, headers=["Fart [m/s]", "Reynoldstall", "C_FS", 
    "Ruhetstillegg", "C_TS", "R_TS [kN]"]))
    print("\n")

    # Henter inn Holtrop formfaktor parametere og beregner motstand
    holtrop_formfaktor_param = get_holtrop_formfaktor_param()
    matrise1_holtrop, matrise2_holtrop, holtrop_factor = holtrop_formfaktor(*holtrop_formfaktor_param)

    # Utskrift av resultater fra Holtrop analyse
    print(tabulate(matrise1_holtrop, headers=["Fart [m/s]", "Motstand [N]", "F_N" ,"Reynoldstall", "C_TM", 
    "C_FM", "C_VM", "C_RM"]))
    print("\n")
    print(tabulate(matrise2_holtrop, headers=["Fart [m/s]", "Reynoldstall", "C_FS", 
    "Ruhetstillegg", "C_TS", "R_TS [kN]"]))
    print("\n")

    # Henter inn Prohaska formfaktor parametere og beregner den
    prohaska_formfaktor_param = get_prohaska_formfaktor_param()
    prohaska_factor = prohaska_formfaktor(*prohaska_formfaktor_param)
    print("\n")

    # Skriver ut sammenligning mellom alle formfaktorer
    print("Sintef Ocean formfaktor:", sintef_factor)
    print("Holtrop formfaktor:\t", holtrop_factor)
    print("Prohaska formfaktor:\t", prohaska_factor)
    print("\n")

    # Finner middelverdien til forskjellen i C_ts
    matriseforskjell = []
    for i in range(len(matrise2_holtrop)):
        matriseforskjell.append(matrise2_holtrop[i][4]-matrise2_sintef[i][4])
    mean_Cts = (max(matriseforskjell)-min(matriseforskjell))/2
    print("Middelverdi:", mean_Cts)
    print("\n")

    # Sammenligner R_ts mot V_s
    # Empirisk, Holtrop
    Rts_eholtrop = holtrop_result[1] / 1000
    Vs_eholtrop = holtrop_result[0] * 1.94384449

    # Empirisk, hollenbach
    Rts_hollenbach = hollenbach_result[1] / 1000
    Vs_hollenbach = hollenbach_result[0] * 1.94384449

    # Modellforsøk Sintef
    Rts_sintef = [matrise2_sintef[i][5] for i in range(len(matrise2_sintef))]
    Vs_sintef = [matrise2_sintef[i][0]*1.94384449 for i in range(len(matrise2_sintef))]

    # Modellforsøk Holtrop
    Rts_holtrop = [matrise2_holtrop[i][5] for i in range(len(matrise2_holtrop))]
    Vs_holtrop = [matrise2_holtrop[i][0]*1.94384449 for i in range(len(matrise2_holtrop))]
    
    plt.title("Sammenligning av motstandsberegninger")
    plt.xlabel("Skipshastighet [knop]")
    plt.ylabel("Motstand [kN]")
    plt.grid(linestyle='-', linewidth=1)
    plt.plot(Vs_eholtrop, Rts_eholtrop, marker='*', label='Empirisk, Holtrop')
    plt.plot(Vs_hollenbach, Rts_hollenbach, marker='*', label='Empirisk, Hollenbach')
    plt.plot(Vs_sintef, Rts_sintef, marker='x', label='Modelltest - Sintef Ocean formfaktor')
    plt.plot(Vs_holtrop, Rts_holtrop, marker='x', label='Modelltest - Holtrop formfaktor')
    plt.legend()
    plt.show()
main()