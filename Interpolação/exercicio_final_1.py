import math

def f(x):
    return (6 * x -5) ** ( 1 / 2)



def integral(x):
    return 9 / (6 * x -5) ** (3 / 2)



def At(a,b):
    return (f (a) + f(b)) * (b - a) * 0.5



def maximo(a, b, ini):
    h = 0
    t = 0
    while True:
        if(a >= b):
            break
        t = integral(a)
        if(t > h):
            h = t
        a = a + ini
    return h



def errr(a, b, numero_divi):
    return ((b - a) ** 3) * maximo(a, b, 0.01) * (1 / (12 * (numero_divi ** 2)))



numero_divi = 100 
ponto_inicial = 1
ponto_final= 9
delta_x = (ponto_final - ponto_inicial) / numero_divi 



a = ponto_inicial 
b = ponto_final + delta_x



resultado = 0
v = 0
while True:
    if(a >= ponto_final):
        break
    resultado = resultado + At(a,b)
    a = b
    b = b + delta_x
    v = v + 1



print(f'A integral aproximado: {resultado:.3f}')
erro = (errr(ponto_inicial, ponto_final, numero_divi))
print(f'O erro aproximado  : {erro:.3f}')