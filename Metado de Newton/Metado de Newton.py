import math

err = 0.00001

def f(x):
    return  0.9/x

def df(x):
    return -0.9 / x**2 
x = -1
while abs (f(x)) > err:
    d = df(x)
    if d == 0:
        d = d + err
    x = x - f(x) / d 

print("Valor aproximado: {:.4f}".format(x))