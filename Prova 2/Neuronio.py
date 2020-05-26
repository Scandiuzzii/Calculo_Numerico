import math
import numpy 
import matplotlib.pyplot

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


DELTA_T = (0.01 * 10 ** (-3)) / (1 * 10 ** (-6))


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
TEMPO.append (T_0 + (0.01 * 10 ** (-3)) )


N = [N_0]
N.append (N_0)
M = [M_0]
M.append (M_0)
H = [H_0]
H.append (H_0)



a = 1 
i = 0
while  i < .25 * 10 ** (-3):
    print (a)
    AUX_N = DN_DT ( AUX_N, V_I [a])
    N.append(AUX_N)
    AUX_M = DM_DT (AUX_M,  V_I [a])
    M.append (AUX_M)
    AUX_H = DH_DT (AUX_H, V_I [a])
    H.append (AUX_H) 


    POTENCIA_N = G_K * (N_0 ** 4) * (V_I [a] - V_K)
    POTENCIA_M = G_NA * (M_0 ** 3) * H_0 * (V_I [a] - V_NA)
    POTENCIA_L = G_L * (V_I [a] - V_L)


    AUX = V_I [a - 1] - (POTENCIA_N + POTENCIA_M + POTENCIA_L) * DELTA_T 
    V_I.append (AUX)  

    a = a + 1 
    i = i + (0.01 * 10 ** (-3))
    TEMPO.append (i)



matplotlib.pyplot.ioff ()
matplotlib.pyplot.plot (TEMPO, V_I ,label = ' V(t) V')
matplotlib.pyplot.xlabel ('tempo (t) s')
matplotlib.pyplot.ylabel ('valores (Tensão(t))')
matplotlib.pyplot.legend ()
matplotlib.pyplot.show  ()


    







