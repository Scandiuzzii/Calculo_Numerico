import math

def f(x):
    return 1 / ((x ** 2) -1)




def integral(x):
    return -2 * (-3 ** 2 - 1) / (x ** 2 - 1) ** 3



def At(a, b):
    return (f (a) + f (b)) * (b - a) * 0.5



def maximo(a, b, ini):
    h = -999
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

numero_divi1 = 8
numero_divi2 = 800
ponto_inicial = 0.0
ponto_final = 0.8
delta_x1 = 0.1
delta_x2 = 0.001
a = ponto_inicial
b = ponto_inicial + delta_x1
resultado1 = 0
a2 = ponto_inicial
b2 = ponto_inicial + delta_x2
resultado2 = 0

while True:
    if(a >= ponto_final):
        break
    resultado1 += At(a, b)
    a = b
    b += delta_x1

    if(a2 >= ponto_final):
        break
    resultado2 += At(a2, b2)
    a2 = b2
    b2 += delta_x2



print('Para h = 0.1')
print('A integral: {}'.format(resultado1))
erro = math.fabs(errr(ponto_inicial, ponto_final, numero_divi1))
print('O erro é: {}\n'.format(erro))



print('Para h = 0.001')
print('A integral: {}'.format(resultado2))
erro = math.fabs(errr(ponto_inicial, ponto_final, numero_divi2))
print('O erro é: {}'.format(erro))