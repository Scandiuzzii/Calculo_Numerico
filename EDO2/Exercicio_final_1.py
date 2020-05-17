import matplotlib.pyplot as plt


def kUM1(a, c):
    return 0.02 * c - 0.03 * a


def kDOIS1(a, c, k1):
    return 0.02 * (c + k1 / 2) - 0.03 * (a + k1 / 2)


def kTRES1(a, c, k2):
    return 0.02 * (c + k2 / 2) - 0.03 * (a + k2 / 2)


def kQUATRO1(a, c, k3):
    return 0.02 * (c + k3) - 0.03 * (a + k3)


def kUM2(a, c):
    return 0.03 * a - (0.01 + 0.02) * c


def kDOIS2(a, c, k1):
    return 0.03 * (a + k1 / 2) - (0.01 + 0.02) * (c + k1 / 2)


def kTRES2(a, c, k2):
    return 0.03 * (a + k2 / 2) - (0.01 + 0.02) * (c + k2 / 2)


def kQUATRO2(a, c, k3):
    return 0.03 * (a + k3) - (0.01 + 0.02) * (c + k3)


h = 0.001
t = 0.1
k11 = 0
k12 = 0
k13 = 0
k14 = 0


k21 = 0
k22 = 0 
k23 = 0
k24 = 0


a = 100 
c = 10
auxa = 0 
auxc = 0


err = 500


plt.ioff()


at=[]
axa=[]
axc=[]


while t < 500:

    
    auxa = a
    auxc = c


    k11 = h * kUM1 (a, c)
    k21 = h * kUM2 (a, c)


    k12 = h * kDOIS1 (a, c, k11)
    k22 = h * kDOIS2 (a, c, k21)


    k13 = h * kTRES1 (a, c, k12)
    k23 = h * kTRES2 (a, c, k22)


    k14 = h * kQUATRO1(a, c, k13)
    k24 = h * kQUATRO2(a, c, k23)


    print('t:{}     a:{}     c:{}     erro:{}'.format(t,a,c,err))
    at.append(t)
    axc.append(c)
    axa.append(a)
    a = a + (k11 + 2 * k12 + 2 * k13 + k14) / 6
    c = c  + (k21 + 2 * k22 + 2 * k23 + k24) / 6
    err = (c - auxa) / auxa + (a - auxc) / auxc
    t = t + h


plt.plot(at, axa, label = 'a') #linha azul
plt.plot(at, axc, label = 'c') #linha laranja
plt.xlabel('tempo (t)')
plt.ylabel(' (a e c)')
plt.title('RK4')
plt.show()