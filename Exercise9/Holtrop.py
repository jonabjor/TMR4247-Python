
# Function for estimating ship resistance using Holtrops empirical method.
# Output is given as a matrix where columns 1,2 and 3 give velocity,
# resistance and power requirement (without accounting for propeller
# efficiency) respectively.
## Input explanation
# Vvec: Velocity vector (m/s). Something like this:[9.8,10,11,12,13,13.5]
# T: Draught at AP
# B: Beam
# L: Length of waterline
# S: Wetted surface of hull
# CP: Prismatic coefficient
# CM: Midship section coefficient
# CB: Block coefficient
# lcb: Longitudinal center of buoyancy measured from 0.5L as percentage of L
# CW: Waterplane area coefficient
# voldispl: Displaced volume [m^3]
# Abt: Transverse bulb area
# Tf: Draught at FP
# hb: Distance of bulb centre of volume from baseline
# At: Area of submerged transom stern
# H: Roughness height [micrometer]
# Stern type indicator:
# Cstern = -25: Pram with gondola
# Cstern = -10: V-shaped sections
# Cstern = 0  : Normal section shape. This can be assumed to be the case here
# Cstern = 10 : U-shaped sections with Hogner stern

import numpy as np
import matplotlib.pyplot as plt

def holtrop(Vvec, T, B, L, S, CP, CM, CB, lcb, CW, voldispl, Abt, Tf, hb, At, H, Cstern):

    # Constants
    g = 9.81                    # Gravity
    rho = 1025                  # Density seawater
    kinvisc = 1.883*10**-6      # Kinetic viscosity

    # Values valid for all velocities - USED IN WAVE MAKING RESISTANCE
    # CALCULATION
    # "Length of run"
    LR = L*(1 - CP + 0.06*CP*lcb/(4*CP - 1))
    iE = 1 + 89*np.exp(-(L/B)**0.80856 * (1 - CW)**0.30484 * (1 - CP - 0.0225*lcb)**0.6367 * (LR/B)**0.34574*(100*voldispl/L**3)**0.16302)
    c3 = 0.56*Abt**1.5/(B*T*(0.31*np.sqrt(Abt) + Tf - hb))
    c2 = np.exp(-1.89*np.sqrt(c3))
    c5 = 1 - 0.8*At/(B*T*CM)
    if L**3/voldispl < 512:
        c15 = -1.69385
    elif L**3/voldispl < 1726.91:
        c15 = -1.69385 + (L/voldispl**(1/3) - 8)/2.36
    else:
        c15 = 0
    
    # c7
    if B/L < 0.11:
        c7 = 0.229577*(B/L)**0.33333
    elif B/L < 0.25:
        c7 = B/L
    else:
        c7 = 0.5 - 0.0625*L/B
    
    # c1
    c1 = 2223105 *c7**3.78613 * (T/B)**1.07961 * (90 - iE)**-1.37565

    # c16
    if CP < 0.8:
        c16 = 8.07981*CP - 13.8673*CP**2 + 6.984388*CP**3
    else:
        c16 = 1.73014 - 0.7067*CP
    
    m1 = 0.0140407*L/T - 1.75254*voldispl**(1/3)/L - 4.79323*B/L - c16
    d = -0.9
    c17 = 6919.3 * CM**-1.3346 * (voldispl/L**3)**2.00977 * (L/B - 2)**1.40692
    m3 = -7.2035 * (B/L)**0.326869 * (T/B)**0.605375
    # Note that the 'lambda' keyword is used in Python to define anomynous functions (not relevant to this).
    # We will therefore use 'my_lambda' to represent the lambda-value.
    if L/B < 12:
        my_lambda = 1.446*CP - 0.03*L/B     
    else:
        my_lambda = 1.446*CP - 0.36
    
    # Correlation factor for resistance - mainly a roughness allowance here
    if Tf/L > 0.04:
        c4 = 0.04
    else:
        c4 = Tf/L
    CA = 0.006*(L + 100)**-0.16 - 0.00205 + 0.003*np.sqrt(L/7.5)*CB**4*c2*(0.04 - c4)
    ks = H*10**-6
    if H > 150:
        CA = CA + (0.105*ks**(1/3) - 0.005579)/L**(1/3)
    CA = 0

    # Preallocating vectors
    FnVec = np.zeros(Vvec.size)
    Rvec = np.zeros(Vvec.size)
    RWAVectorOuter = np.zeros(Vvec.size)
    CWAVector = np.zeros(Vvec.size)

    Vcounter = 0
    for V in Vvec:
        # WAVE MAKING RESISTANCE
        FnOrig = V/np.sqrt(g*L)
        FnVec[Vcounter] = FnOrig

        if FnOrig > 0.4 and FnOrig < 0.5:
            FnVecInner = np.array([0.4, 0.55])
        else:
            FnVecInner = np.array([FnOrig])
        
        RWAVectorInner = np.zeros(FnVecInner.size)
        FnCounter = 0
        for Fn in FnVecInner:
            m4 = c15*0.4*np.exp(-0.034*Fn**-3.29)

            if Fn < 0.4:
                RWAVectorInner[FnCounter] = c1*c2*c5*voldispl*rho*g*np.exp(m1*Fn**d + m4*np.cos(my_lambda*Fn**(-2)))
            elif Fn > 0.5:
                RWAVectorInner[FnCounter] = c17*c2*c5*voldispl*rho*g*np.exp(m3*Fn**d + m4*np.cos(my_lambda*Fn**(-2)))
            
            FnCounter += 1

        if RWAVectorInner.size > 1:
            # This only happens if Fn is between 0.4 and 0.5. Then the first
            # entry in RWA is for Fn = 0.4 and the second is for Fn = 0.55
            RWA = RWAVectorInner[0] + (FnOrig - 0.4)*(RWAVectorInner[1] - RWAVectorInner[0])/1.5
        else:
            RWA = RWAVectorInner[0]

            RWAVectorOuter[Vcounter] = RWA

        # RESISTANCE DUE TO BULBOUS BOW
        PB = 0.56*np.sqrt(Abt)/(T - 1.5*hb)
        FNI = V/np.sqrt(rho*(Tf - hb - 0.25)*np.sqrt(Abt) + 0.15*V**2)
        RB = 0.11*np.exp(-3*PB**-2)*FNI**3*Abt*1.5*rho*g/(1 + FNI**2)
        
        # RESISTANCE DUE TO TRANSOM STERN
        FNT = V/np.sqrt(2*g*At/(B + B*CW))
        if FNT < 5:
            c6 = 0.2*(1 - 0.2*FNT)
        else:
            c6 = 0
        RTR = 1/2*rho*V**2*c6

        # FRICTIONAL RESISTANCE ON HULL 
        # Estimated wetted surface:
        S_estimate = L*(2*T + B)*np.sqrt(CM)*(0.453 + 0.4425*CB - 0.2862*CM - 0.00346*B/T + 0.3696*CW) + 2.38*Abt/CB
        S_estimate = S
        c14 = 1 + 0.011*Cstern
        k = -1 + 0.93 + 0.487118*c14*(B/L)**1.06806*(T/L)**0.46106*(L/LR)**0.121563*(L**3/voldispl)**0.36486*(1 - CP)**-0.604247

        Rn = V*L/kinvisc
        CF = 0.075/(np.log10(Rn)-2)**2
        # deltaCF = (111*(H*V)**0.21 - 404)*CF**2; # Not used in Holtrop. CA used instead

        RF = 1/2*rho*V**2*S_estimate*CF*(1 + k)

        # CORRELATION FACTOR RESISTANCE (Mainly roughness allowance)
        RA = 1/2*rho*V**2*S_estimate*CA

        # TOTAL RESISTANCE AT GIVEN SPEED
        Rvec[Vcounter] = RWA + RB + RF + RTR + RA

        CWAVector[Vcounter] = RWA/(1/2*rho*V**2*S)

        Vcounter += 1
    
    Pvec = np.multiply(Rvec, Vvec)   # Propulsion power required for keeping the ship moving at the specific speed (without accounting for propeller losses)
    '''
    # Figure 1
    plt.figure()
    plt.plot(FnVec, CWAVector)
    ax = plt.gca()
    ax.set(xlabel = 'Froude Number', ylabel = 'CWA',
       title = 'Wave making resistance coefficient, Holtrops method')

    # Figure 2
    plt.figure()
    plt.plot(Vvec*3600/1852, Rvec/1000)
    ax = plt.gca()
    ax.set(xlabel = 'Velocity [knots]', ylabel = 'Resistance [kN]',
        title = 'Total Resistance, Holtrops method')

    plt.show()
    '''
    return np.array([Vvec, Rvec, Pvec])
    
            
    


