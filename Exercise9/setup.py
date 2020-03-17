import numpy as np

# Values to be used in the calculations. Set the values here [global scope]

# Ship fullscale values     
Vvec_s = np.array([10.3,10.8,11.3,11.8,12.3,12.8,13.3]) # Vvec = Velocity vector [m/s]
Tap_s = 11 # Tap = Draught at AP [m]
Tfp_s = 11 # Tfp = Draught at FP [m]
B_s = 32.2 # B = Beam [m]
Lpp_s = 233 # Lpp = Length between perpendiculars [m]
Los_s = 234.526 # Los = Length over Surface [m]
Lwl_s = 227.953 # Lwl = Length of waterline [m]
S_s = 9203.90 # S = Wetted surface of hull [m^2]
Cd_s = 0.82 # Cd_s = Air drag coefficient [-]
v_s = 1.883*10**(-6) # v_s = Kinematic viscosity [m^2/s]
ro_s = 1025 # ro_s = Density of salt water [kg/m^3]
voldispl = 49842.8 # voldispl = Displaced volume [m^3]
Abt = 0 # Abt = Transverse bulb area [m^2]
hb = 0 # hb = Distance of bulb centre of volume from baseline [m]
At = 0 # At = Area of submerged transom stern [m^2]
At_s = 850 # At_s = Cross sectional area of hull over water [m^2]
H_s = 150 # H = Roughness height [micrometer]
Cstern = 0 # Stern type indicator [-]

Dp = 1 # Dp = Propelldiameter [m]
NRud = 1 # Nrud = Antall ror [-]
NBrac = 0 # NBrac = Antall braketter [-]
NBoss = 0 # NBoss = Antall propellboss [-]
NThr = 0 # NThr = Antall tunnelthrustere [-]

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
T_m = 0.289 # T_m = Draught [m]
displ_m = 0.908 # displ_m = volume displacement [m^3]

# Towing test results
V_m = np.array([1.666, 1.758, 1.84, 1.925, 2.005, 2.092, 2.182]) # V_m = Velocities used in towing test [m/s]
R_tm = np.array([32.167, 36.169, 40.27, 45.097, 50.2225, 56.859, 64.874]) # Resistances [N] for the corresponding velocities in V_m

# Ship general constants
Cp = 0.6216 # CP = Prismatic coefficient [-]
Cm = 0.9717 # CM = Midship section coefficient [-]
Cb = 0.6039 # CB = Block coefficient [-]
Cw = 0.804 # CW = Waterplane area coefficient [-]
lcb = -2.236 # lcb = Longitudinal center of buoyancy measured from 0.5L as percentage of L [% Lpp]

# Misc constants
ro_a = 1.25 # Density of air [kg/m^3]
Ca = -0.23*10**(-3) # Correlation coefficient [-]

# end of values ----------------------------------------------------------------------------------------

def get_holtrop_param():
    return Vvec_s, Tap_s, B_s, Lwl_s, S_s, Cp, Cm, Cb, lcb, Cw, voldispl, Abt, Tfp_s, hb, At, H_s, Cstern

def get_hollenbach_param(): 
    return Vvec_s, Lpp_s, Lwl_s, Los_s, B_s, Tfp_s, Tap_s, Cb, S_s, Dp, NRud, NBrac, NBoss, NThr

def get_sintef_formfaktor_param():
    return (V_m, R_tm, Vvec_s, ro_a, Cb, Ca, Tap_m, Tfp_m, Lwl_m, B_m, 
    S_m, Cd_m, H_m, At_m, v_m, ro_m, Tap_s, Tfp_s, Lwl_s, B_s, 
    S_s, Cd_s, H_s, At_s, v_s, ro_s)

def get_holtrop_formfaktor_param():
    # Constant calculated from model values
    L_r = Lwl_m *(1-Cp+0.06*Cp*lcb/(4*Cp-1))
    return (V_m, R_tm, Vvec_s, ro_a, Cb, Cp, Ca, Lwl_m, B_m, T_m, ro_m, S_m, v_m, Cd_m, H_m
    , At_m, lcb, displ_m, Lwl_s, B_s, ro_s, S_s, v_s, Cd_s, H_s
    , At_s, L_r)

def get_prohaska_formfaktor_param():
    return (V_m, R_tm, Lwl_m, v_m, ro_m, S_m)
