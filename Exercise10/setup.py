import numpy as np
s = 1.2 # Spenn [m]
c = 0.4 # Korde [m]
k = 2 # Konstant grunnet speilingseffekt foil/skrog [-]
V = np.array([10,15,20]) # Hastighet [m/s]
L = 15000 # Løftkraft [N]
rho = 1025 # Tetthet saltvann [kg/m^3]
v = 1.19*10**(-6) # Kinematisk viskositet 
t_max = 0.1 # Maks tykkelse foil [m]

def get_angrepsvinkel_param():
    return (s, c, V, L, rho, k)

def get_motstandsberegning_param():
    return (s, c, V, L, rho, k, v, t_max)