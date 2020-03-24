import numpy as np
from calculation import angrepsvinkel, motstandsberegning
from setup import get_angrepsvinkel_param, get_motstandsberegning_param
from tabulate import tabulate

def main():
    #-------------- Angrepsvinkel beregninger --------------
    V, alpha = angrepsvinkel(*get_angrepsvinkel_param())
    matrix = np.transpose([V,alpha,np.rad2deg(alpha)])
    print(tabulate(matrix, headers=["Hastighet[m/s]", "Alpha[rad]", "Alpha[deg]"]))

    #-------------- Motstandsberegninger --------------
    V, Rn, Cl, Cdi, Cf, Cdv, Cd, Fd = motstandsberegning(*get_motstandsberegning_param())
    matrix = np.transpose([V, Rn,Cl,Cdi,Cf,Cdv,Cd,Fd])
    print(tabulate(matrix, headers=["Hastighet", "Rn", "C_L", "C_DI", "C_F", "C_DV", "C_D", "F_D"]))
main()