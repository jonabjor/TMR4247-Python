import numpy as np
from scipy import stats
from tabulate import tabulate

def linregfriprove(Ktt_f, Kq_f, J_f, Ktt):
    x = J_f
    y = Ktt_f
    # Lineær regresjon av Ktt fra friprøve. Løser x for y = Ktt for å finne J0
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    J0 = (Ktt - intercept) / slope
    # Linær regresjon av Kq fra friprøve. Løser y-verdi for x = J0 for å finne Kq0
    y = Kq_f
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    Kq0 = intercept + slope*J0

    return J0, Kq0

def propulsjonsprove(Ktt_f, Kq_f, J_f):
    # Misc data
    rho = 1000 # Tetthet ferskvann [kg/m^3]

    # Data fra propulsjonsprøve
    V = np.array([0.6408,0.9612,1.2807,1.6011,1.9216,2.0818]) # Modellens hastighet
    n1 = np.array([3.185,4.7744,6.4136,8.2952,10.7099,12.2479]) # Turtall propell 1 [1/s]
    n2 = np.array([3.1813,4.77,6.4102,8.2933,10.7085,12.2446]) # Turtall propell 2 [1/s]
    Tp1 = np.array([2.9175,6.8181,13.0123,23.0699,42.6015,58.4303]) # Thrust propell 1 [N]
    Tp2 = np.array([2.8101,6.5444,12.3482,21.7394,40.2424,55.5292]) # Thrust propell 2 [N]
    Td1 = np.array([-0.161,-0.3048,-0.1064,0.8563,4.1522,7.5998]) # Thrust dyse 1 [N]
    Td2 = np.array([-0.1847,-0.3788,-0.2753,0.3311,3.6355,6.8534]) # Thrust dyse 2 [N]
    Q1 = np.array([0.1323,0.2971,0.5494,0.9528,1.6963,2.2922]) # Dreiemoment propell 1 [Nm]
    Q2 = np.array([0.1246,0.2774,0.5145,0.8909,1.6029,2.1777]) # Dreiemoment propell 2 [Nm]
    Fs = np.array([1.7964,3.6549,5.6723,7.8674,10.2310,11.4540]) # Snordrag [N]

    # Data fra slepeprøve
    Rtm = np.array([6.587, 13.956, 25.406, 42.427, 76.671, 107.401]) # Modellens motstand [N] for akutelle hastigheter

    # Propelldata
    D = 0.19333 # Propelldiameter [m]
    ant = 2 # Antall dysepropeller [1]

    # Snordrag og motstand skalering
    Fs = Fs / ant
    Rtm = Rtm / ant

    # Thrustberegninger og dreiemoment
    Tp = Tp1 + Tp2 # Total thrust propell
    Td = Td1 + Td2 # Total thrust dyse
    Q = Q1 + Q2 # Totalt dreiemoment på propell

    # Beregning av thrustkoeffisientene (Ktp, Ktd og Ktt)
    Ktp = ((Tp) / (rho * (n1+n2)**2 * D**4 ))
    Ktd = ((Td) / (rho * (n1+n2)**2 * D**4 ))
    Ktt = Ktp + Ktd

    # Beregning av J og Kq
    Kq = ((Q) / (rho * (n1+n2)**2 * D**5))
    J = V / (((n1+n2)/2)*D)

    # Beregning av thrustreduksjon
    t = ((Tp+Td)/2 - Rtm + Fs) / ((Tp+Td)/2)

    # Bruker beregnet Ktt fra propulsjonsprøven til å gå inn i friprøvediagram og lese av J0 og Kq0. 
    # Løser det ved hjelp av lineær interpolasjon av resultat fra friprøvediagram.
    J0, Kq0 = linregfriprove(Ktt_f, Kq_f, J_f, Ktt)
    Kq0 *= 10
    # Beregning av effektiv medstrøm
    wm = 1 - J0/J

    # Beregning av relativ rotasjonsvirkningsgrad
    hr = Kq0 / Kq

    # Beregning av skrogvirkningsgrad
    hh = (1-t)/(1-wm)

    return (V, J, Ktt, Kq, J0, Kq0, wm, hr, t, hh)

def printpropulsjon(V, J, Ktt, Kq, J0, Kq0, wm, hr, t, hh):
    matrix = np.array([V, J, Ktt, Kq, J0, Kq0, wm, hr, t, hh])
    matrix = np.transpose(matrix)
    print(tabulate(matrix, headers=["V", "J", "Kt", "Kq", "J0", "Kq0", "wm", "hr", "t", "hh"]))

