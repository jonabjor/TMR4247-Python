from setup import get_holtrop_param, get_hollenbach_param, get_sintef_formfaktor_param
from Holtrop import holtrop
from Hollenbach import hollenbach
def main():
    # Henter inn Holtrop parametere og kaller på holtrop funksjonen
    holtrop_param = get_holtrop_param()
    #holtrop_result = holtrop(*holtrop_param)

    # Henter inn Hollenbach parametere og kaller på holtrop funksjonen
    hollenbach_param = get_hollenbach_param()
    #hollenbach_result = hollenbach(*hollenbach_param)

    sintef_formfaktor_param = get_sintef_formfaktor_param()
    print(sintef_formfaktor_param)
main()