import math 

def newton (f,flin,x0,epsilon,maxIter=10000):
    if abs(f(x0))<= epsilon:
        return x0
    print ("iter\t\t x0\t\t\t f(x0)")
    iter = 1 
    while iter<= maxIter:
        x1 = x0 - f(x0) / flin(x0)
        print("%d\t\t %e\t\t %e\t\t" %(iter,x1,f(x1)))
        if abs (f(x1))<= epsilon:
            return x1 
        x0 = x1
        iter = iter +1 
    print("EROO: Número máximo de interações atingido")
    return x1

if __name__ == "__main__":
    def f(x):
        return 0.9/ x  
    def flin(x):
        return  -0.9 / x*x
raiz = newton(f,flin,-1,0.001)
print("Valor aproximado: {:.4f}".format(raiz))