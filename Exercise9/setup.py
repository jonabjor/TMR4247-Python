import numpy as np

def get_holtrop_param():
    Vvec = np.array([10.3,10.8,11.3,11.8,12.3,12.8,13.3]) # Vvec: Velocity vector [m/s]
    T = 11 # T: Draught at AP [m]
    B = 32.2 # B: Beam [m]
    L = 227.953 # L: Length of waterline [m]
    S = 9203.90 # S: Wetted surface of hull [m^2]
    CP = 0.6216 # CP: Prismatic coefficient [-]
    CM = 0.9717 # CM: Midship section coefficient [-]
    CB = 0.6039 # CB: Block coefficient [-]
    lcb = -2.236 # lcb: Longitudinal center of buoyancy measured from 0.5L as percentage of L [% Lpp]
    CW = 0.804 # CW: Waterplane area coefficient [-]
    voldispl = 49842.8 # voldispl: Displaced volume [m^3]
    Abt = 0 # Abt: Transverse bulb area [m^2]
    Tf = 11 # Tf: Draught at FP [m]
    hb = 0 # hb: Distance of bulb centre of volume from baseline [m]
    At = 0 # At: Area of submerged transom stern [m^2]
    H = 150 # H: Roughness height [micrometer]
    Cstern = 0 # Stern type indicator [-]
    return Vvec, T, B, L, S, CP, CM, CB, lcb, CW, voldispl, Abt, Tf, hb, At, H, Cstern

def get_hollenbach_param():
    Vsvec = np.array([10.3,10.8,11.3,11.8,12.3,12.8,13.3]) # Vsvec: Velocity vector [m/s]
    L = 233 # L = Length between perpendiculars [m]
    Lwl = 227.953 # Lwl = Length of waterline [m]
    Los = 234.526 # Los = Length over Surface [m] 
    B = 32.2 # B = Beam [m]
    TF = 11 # TF = Dypgang ved FP [m]
    TA = 11 # TA = Dypgang ved AP [m]
    CB = 0.6039 # CB = Block coefficient [-]
    S = 9203.90 # S = Wetted surface of hull [m^2]
    Dp = 1 # Dp = Propelldiameter [m]
    NRud = 1 # Nrud = Antall ror [-]
    NBrac = 0 # NBrac = Antall braketter [-]
    NBoss = 0 # NBoss = Antall propellboss [-]
    NThr = 0 # NThr = Antall tunnelthrustere [-]
    return Vsvec, L, Lwl, Los, B, TF, TA, CB, S, Dp, NRud, NBrac, NBoss, NThr

def get_sintef_formfaktor_param():
    # Results from towing test
    V_m = np.array([1.666, 1.758, 1.84, 1.925, 2.005, 2.092, 2.182]) # V_m = Velocities used in towing test [m/s]
    R_tm = np.array([32.167, 36.169, 40.27, 45.097, 50.2225, 56.859, 64.874]) # Resistances [N] for the corresponding velocities in V_m
    
    # Velocities to be used for fullscale model
    V_s = np.array([10.3,10.8,11.3,11.8,12.3,12.8,13.3]) # Velocities [m/s]

    # Constants for the ship, independent of model/fullscale
    ro_a = 1.25 # Density of air [kg/m^3]
    Cb = 0.6039 # Block coefficient [-]
    Ca = -0.23*10**(-3) # Correlation coefficient [-]

    # Model values
    Tap_m = 0.289 # Tap_m = Draught at AP [-]
    Tfp_m = 0.289 # Tfp_m = Draught at FP [-]
    Lwl_m = 5.999 # Lwl_m = Length of waterline [m]
    B_m = 0.847 # B_m = Beam [m]
    S_m = 6.374 # S_m = Wetted surface of hull [m^2]
    Cd_m = 0.82 # Cd_m = Air drag coefficient [-]
    H_m = 0 # H_m = Roughness height [micrometer]
    At_m = 0.25 # At_m = Cross sectional area of hull over water [m^2]
    v_m = 1.1395*10**(-6) # v_m = Kinematic viscosity [m^2/s]
    ro_m = 1000 # ro_m = Density of freshwater [kg/m^3]

    # Fullscale ship values
    Tap_s = 11 # Tap_s = Draught at AP [-]
    Tfp_s = 11 # Tfp_s = Draught at FP [-]
    Lwl_s = 227.953 # Lwl_s = Length of waterline [m]
    B_s = 32.2 # B_s = Beam [m]
    S_s = 9203.9 # S_s = Wetted surface of hull [m^2]
    Cd_s = 0.82 # Cd_s = Air drag coefficient [-]
    H_s = 150 # H_s = Roughness height [micrometer]
    At_s = 850 # At_s = Cross sectional area of hull over water [m^2]
    v_s = 1.883*10**(-6) # v_s = Kinematic viscosity [m^2/s]
    ro_s = 1025 # ro_s = Density of salt water [kg/m^3]
    return (V_m, R_tm, V_s, ro_a, Cb, Ca, Tap_m, Tfp_m, Lwl_m, B_m, 
    S_m, Cd_m, H_m, At_m, v_m, ro_m, Tap_s, Tfp_s, Lwl_s, B_s, 
    S_s, Cd_s, H_s, At_s, v_s, ro_s) 