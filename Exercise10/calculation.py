import numpy as np

def angrepsvinkel(s, c, V, L, rho, k):
    Asp = s / c # Aspektforhold, forhold mellom spenn og korde midlet over spennet [-]
    Ap = 2 * s * c # Projisert areal [m^2]
    Cl = L / (1/2 * rho * V**2 *Ap) # Løftkoeffisient [-]
    alpha = Cl * (1+ 2 / (k*Asp)) * 1/(2*np.pi) # Angrepsvinkel [rad]
    return V, alpha

def motstandsberegning(s, c, V, L, rho, k, v, t_max):
    Asp = s / c # Aspektforhold, forhold mellom spenn og korde midlet over spennet [-]
    Ap = 2 * s * c # Projisert areal [m^2]
    Cl = L / (1/2 * rho * V**2 *Ap) # Løftkoeffisient [-]

    # Beregning av indusert motstand (Cdi)
    Cdi = Cl**2 / (np.pi * Asp) # Indusert motstand

    # Beregning av visøks motstand (Cdv)
    Rn = (V*c)/ v # Reynoldstallet
    Cf = 0.075 / (np.log10(Rn)-2)**2 # Friksjonskoeffisienten (ITTC)
    Cdv = 2*(1+2*(t_max/c))*Cf # Viskøs motstand

    # Beregning av totalmotstand
    Cd = Cdv + Cdi
    Fd = Cd * (rho / 2) * V**2 * Ap
    return V, Rn, Cl, Cdi, Cf, Cdv, Cd, Fd
