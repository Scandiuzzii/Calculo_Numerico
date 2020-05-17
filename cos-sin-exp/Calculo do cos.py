
import math

def cosseno(x,y):
    a = 0
    b = 0

    x = x/180*math.pi

    while a <= y:
        b += (math.pow(-1,a) / math.factorial(2 * a)) * math.pow(x,(2*a))
        a += 1
    return b

def erro(esperado,obtido):
    return math.fabs(((obtido - esperado) / esperado)) * 100

cos = int(input("digite um valor para cos "))

print("Valor real de cosseno eh: {}".format(math.cos(cos)))
print("valor calculado de cosseno para 1 interação eh: {} e para 10 eh de: {}".format(cosseno(cos,1),cosseno(cos,10)))
print("Erro obtido de cosseno para 1 interação eh: {}'%' e para 10 eh de {}'%'\n".format(erro(math.cos(cos),cosseno(cos,1)),erro(math.cos(cos),cosseno(cos,10))))

