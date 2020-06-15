import math

err = 0.00001


def f(T):
    return 0.9 * 900 - (0.15 * ( 5.67 * 10**(-8)) * T**4 + 5 * (T - 300)) 


def df(T):
    return 0-((0.15 * ( 5.67 * 10**(-8))* 4*T**3 ) + 5)

 
T = 400
while abs (f(T)) > err:
    d = df(T)
    if d == 0:
        d = d + err
    T = T - f(T) / d
    

print("Valor aproximado em K: {:.3f}\n".format(T))

T_celsius = T - 273.15 
print("Valor aproximado em °C: {:.3f}".format(T_celsius))