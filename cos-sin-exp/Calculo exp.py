import math

def exp(x,y):
    a = 0
    b = 0

    while a <= y:
        b += (x**a) / math.factorial(a)
        a += 1
    
    return b


def erro(esperado,obtido):
    return math.fabs(((obtido - esperado) / esperado)) * 100

e = int(input("\ndigite um valor para e "))

print("\nValor real de e eh: {}".format(math.exp(e)))
print("valor calculado de e para 1 interação eh: {} e para 10 eh de: {}".format(exp(e,1),exp(e,10)))



