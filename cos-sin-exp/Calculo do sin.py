
import math

def sen (x,y):

    a = 0 #integração
    b = 0 #somador

    x = x/180*math.pi

    while a <= y:
        b += (-1**a / math.factorial(2 * a + 1)) * (x**(2 * a + 1))
        a += 1
    return b


def erro(esperado,obtido):
    return math.fabs(((obtido - esperado) / esperado)) * 100

seno = int(input("digite um valor para sen "))


print("Valor real de seno é: {}".format(math.sin(seno)))
print("valor calculado de seno para 1 interação eh: {} e para 10 eh de: {}".format(sen(seno,1),sen(seno,10)))
print("Erro obtido de seno para 1 interação: {}'%' e para 10 de {}'%'\n".format(erro(math.sin(seno),sen(seno,1)),erro(math.sin(seno),sen(seno,10))))