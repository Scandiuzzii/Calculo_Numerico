import math

#função = f(x) = 10cos(x) em x = pi / 6


def erro (x, h):
    return (h ** 2 / 2) * -1 * math.cos (x) + (h ** 3 / 6) * math.sin (x) + (h ** 4 / 24) * math.cos (x)


def funcaoX (x):
    return math.cos(x)


def DFDX (h):
    print (f'deltaX = {h}')
    
    
    print ('Diferenças Progressivas:')
    dfdx = -10 * ( ( funcaoX (x + h) - funcaoX (x) ) / h + erro (x, h) )
    print (f'df/dx = {dfdx}')
    print (f'ER% = {(sol_exata - dfdx) * 100 / sol_exata} % \n')


    print ('Diferenças Atrassada:')
    dfdx = -10 * ( ( funcaoX (x) - funcaoX(x - h) ) / h + erro (x, h) )
    print (f'df/dx = {dfdx}')
    print (f'ER% = {(sol_exata - dfdx) * 100 / sol_exata} % \n')


    print ('Diferenças Centrais:')
    dfdx = -10 * ( ( funcaoX (x + h) - funcaoX (x - h) ) / 2 * h + (10 * erro (x, h)) ** 2 )
    print (f'df/dx = {dfdx}')
    print (f'ER% = {(1 - (sol_exata - dfdx) / sol_exata) * 100} % \n\n')
    

x = ((math.pi / 6) * 57.2958)
sol_exata = 10 * math.sin(x)


h1 = 0.1
h2 = 0.02
h3 = 0.0001


DFDX (h1)
DFDX (h2)
DFDX (h3)