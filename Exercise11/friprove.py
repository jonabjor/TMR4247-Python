import numpy as np
import matplotlib.pyplot as plt

def friprove():
    # Data for propell og friprøve
    n = 11.98 # Turtall [o/s]
    rho = 1000 # Tetthet ferskvann [kg/m^3]
    D = 0.19333 # Propelldiameter [m]
    V = np.array([0,0.232,0.463,0.695,0.926,1.158,1.390,1.621,1.853,2.084,2.316,2.548,2.779]) # Fremgangshastighet [m/s]
    Tp = np.array([73.783,72.380,70.575,68.169,64.761,60.350,54.937,48.320,40.501,31.278,20.651,8.020,-7.418]) # Thrust fra propell [N]
    Td = np.array([64.36,53.934,43.308,33.684,25.062,17.844,11.428,5.614,0,-6.015,-12.631,-19.849,-26.867]) # Thrust fra dyse [N]
    Q = np.array([2.81,2.729,2.663,2.585,2.477,2.333,2.155,1.934,1.678,1.38,1.035,0.628,0.128]) # Dreiemoment [Nm]

    # Beregning av fremgangstall [J]
    J = (V / (n*D)) # Fremgangstall for propellen [-]

    # Beregning av momentkoeffisient [Kq]
    Kq = (Q / (rho * n**2 * D**5)) # Momentkoeffisient [-]

    # Beregning av thrustkoeffisientene Ktp, Ktd, Ktt
    Ktp = (Tp / (rho * n**2 * D**4)) # Thrustkoeffisient for propell [-]
    Ktd = (Td / (rho * n**2 * D**4)) # Thrustkoeffisient for dyse [-]
    Ktt = Ktp + Ktd # Thrustkoeffisient for propell+dyse [-]

    # Beregning av virkningsgrad h0
    h0 = (J / (2*np.pi)) * (Ktt / Kq)

    return Ktp, Ktd, Ktt, Kq, h0, J

def plotfriprove(Ktp, Ktd, Ktt, Kq, h0, J):
    plt.title(r'Friprøvediagram')
    plt.plot(J, Ktt, label=r'$K_{TT}$')
    plt.plot(J, 10*Kq, label=r'$10*K_{Q}$')
    #plt.plot(J, Ktp, label=r'$K_{TP}$')
    #plt.plot(J, Ktd, label=r'$K_{TD}$')
    plt.plot(J[:-3], h0[:-3], label=r'$\eta_0$')
    plt.legend()
    plt.xlim([0.25,1.4])
    plt.ylim([0,0.9])
    plt.xlabel("J")
    plt.show()