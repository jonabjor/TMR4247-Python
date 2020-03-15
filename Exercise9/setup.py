import numpy as np

def get_holtrop_param():
    Vvec = np.array([10.3,10.8,11.3,11.8,12.3,12.8,13.3]) # Vvec: Velocity vector (m/s)
    T = 11 # T: Draught at AP
    B = 32.2 # B: Beam
    L = 227.953 # L: Length of waterline
    S = 9203.90 # S: Wetted surface of hull
    CP = 0.6216 # CP: Prismatic coefficient
    CM = 0.9717 # CM: Midship section coefficient
    CB = 0.6039 # CB: Block coefficient
    lcb = -2.236 # lcb: Longitudinal center of buoyancy measured from 0.5L as percentage of L
    CW = 0.804 # CW: Waterplane area coefficient
    voldispl = 49842.8 # voldispl: Displaced volume [m^3]
    Abt = 0 # Abt: Transverse bulb area
    Tf = 11 # Tf: Draught at FP
    hb = 0 # hb: Distance of bulb centre of volume from baseline
    At = 0 # At: Area of submerged transom stern
    H = 150 # H: Roughness height [micrometer]
    Cstern = 0 # Stern type indicator
    return Vvec, T, B, L, S, CP, CM, CB, lcb, CW, voldispl, Abt, Tf, hb, At, H, Cstern

def get_hollenbach_param():
    Vsvec = np.array([10.3,10.8,11.3,11.8,12.3,12.8,13.3]) # Vsvec: Velocity vector [m/s]
    L = 233 # L = Length between perpendiculars [m]
    Lwl = 227.953 # Lwl = Length of waterline [m]
    Los = 234.526 # Los = Length over Surface [m] 
    B = 32.2 # B = Beam [m]
    TF = 11 # TF = Dypgang ved FP [m]
    TA = 11 # TA = Dypgang ved AP [m]
    CB = 0.6039 # CB = Block coefficient
    S = 9203.90 # S = Wetted surface of hull
    Dp = 1 # Dp = Propelldiameter [m]
    NRud = 1 # Nrud = Antall ror [-]
    NBrac = 0 # NBrac = Antall braketter [-]
    NBoss = 0 # NBoss = Antall propellboss [-]
    NThr = 0 # NThr = Antall tunnelthrustere [-]
    return Vsvec, L, Lwl, Los, B, TF, TA, CB, S, Dp, NRud, NBrac, NBoss, NThr