import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from tabulate import tabulate

def effektbehov(Ktt, Ktq, J, wm, t, hr):
    # Inndata
    Vm = np.array([0.640, 0.960, 1.280, 1.599, 1.919, 2.079]) # Hastighet modell [m/s]
    Vs = np.array([4, 6, 8, 10, 12, 13]) * 0.5144 # Hastighet fullskala [m/s]
    Rts = np.array([5.37, 11.62, 22.30, 39.10, 75.29, 108.79])*10**3 # Fullskala motstand [N]
    
    rho_s = 1025 # Tetthet saltvann [kg/m^3]
    D = 0.19333 * 10.345 # Propelldiameter [m]

    # Beregnet Kt/J**2
    num = Rts / (rho_s * (1-t) * D**2 * Vs**2 * (1-wm)**2)

    # Beregnet J*
    Jstar = ktt_J_curve(Ktt, J, num)
    
    # Beregner Jq* som hører til J*
    p = np.poly1d(np.polyfit(J[:-1], Ktq[:-1], 1))
    Kqstar = p(Jstar)
    
    # Beregner fullskala turtall
    rpm = ((60*(1-wm)) / D) * (Vs / Jstar)
    
    # Beregner fullskala effekt levert til propell
    Pd = ((2*np.pi) / 1000) * rho_s * D**5 * ((rpm/60)**3) * (Kqstar / hr)
    
    return Vs, num, Jstar, Kqstar, rpm, Pd

def ktt_J_curve(Ktt, J, num):
    # Plot av KT/J^2 kurven som skal brukes i interpoleringen,
    # kommenteres ut etter interpolering ok
    # plt.title(r'$K_T/J^2$-kurve')
    # plt.plot(np.copy(Ktt/J**2)[1:5], (np.copy(J))[1:5], marker="o")
    # plt.xlabel(r'$K_T/J^2$')
    # plt.ylabel(r'$J*$')
    # plt.xlim([0,10])
    
    # Tar en polynomtilpasning:
    x = np.copy(Ktt/J**2)[1:5]
    y = np.copy(J)[1:5]
    p = np.poly1d(np.polyfit(x, y, 1))

    Jstar = p(num)
    return Jstar

def printeffektbehov(Vs, Jstar, Kqstar, rpm, Pd):
    matrix = np.array([Vs*1.94384449, Jstar, Kqstar, rpm, Pd])
    matrix = np.transpose(matrix)
    print(tabulate(matrix, headers=["Hastighet [knop]", "J*", "Kq*", "RPM", "PD [kW]"]))

def finnHastOgTurtall(Vs, rpm, Pd):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(Vs, Pd, 'b-')
    ax1.set_xlabel('Skipshastighet [knop]')
    ax1.set_ylabel('Akseleffekt [kW]')

    ax2 = ax1.twinx()
    ax2.plot(Vs, rpm, marker="o")
    ax2.set_ylabel('Turtall [1/s]')
    plt.show()