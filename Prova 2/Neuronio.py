import math

def ALFA_N (vm):
    return (0.01 * (vm - 10) ) / (math.exp ( ( vm - 10) / 10) - 1) 


def ALFA_M (vm):
    return (0.01 * (vm - 25) ) / (math.exp ( ( vm - 25) / 10) - 1)


def ALFA_H (vm):
    return 0.07 * math.exp (vm / 20)


def BETA_N (vm):
    return 0.125 * math.exp (vm / 80)


def BETA_M (vm):
    return 4 * math.exp ( vm / 18)


def BETA_H (vm):
    return 1 / (math.exp ( ( vm - 30) / 10) + 1)



def DN_DT (n, vm):
    return n + (0.01 * 10 **(-3))  *  ( ALFA_N (vm) * (1 - n) - BETA_N (vm) * n) 


def DM_DT (m, vm):
    return m + (0.01 * 10 **(-3)) *  ( ALFA_M (vm) * (1 - m) - BETA_M (vm) * m) 


def DH_DT (h, vm):
    return h +  (0.01 * 10 **(-3)) * ( ALFA_H (vm) * (1 - h) - BETA_H (vm) * h)


V_K = -77 * 10 ** (-3)
V_NA = 50 * 10 ** (-3)
V_L = -54.402 * 10 ** (-3)


G_K = 3.60
G_NA = 12
G_L = 0.03


N_0 = 0.3176
M_0 = 0.0529 
H_0 = 0.5961


V_0 = -65.002 * 10 ** (-3)
T_0 = 0


AUX_N = N_0
AUX_M = M_0
AUX_H = H_0


T = float(input ('Valor de deltaT: ') ) * 10 ** (-3) 
DELTA_T = T / 1 * 10 ** (-6) 


V_I = [] #tensão
V_I.append (V_0)
TEMPO = []
TEMPO.append (T_0)


# S(VI) = gK * n^4 (VI - VK) + gNA * m^3 * h + (VI - vNA) + gL (VI - VL) # Escolhi sperar essa expressão para maior entendemento e facilidade para programação


POTENCIA_N = G_K * (N_0 ** 4) * (V_I [0] - V_K)
POTENCIA_M = G_NA * (M_0 ** 3) * H_0 * (V_I [0] - V_NA)
POTENCIA_L = G_L * (V_I [0] - V_L)


VI_TOTAL = V_I [0] - (POTENCIA_N + POTENCIA_M + POTENCIA_L) * DELTA_T
V_I.append (VI_TOTAL)
TEMPO.append (T_0 + T)







