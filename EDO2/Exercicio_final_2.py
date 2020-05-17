import matplotlib.pyplot as plt


def kUM1(a, b, c):
    return 0.08 * c + 0.02 * b - 0.03 * a


def kDOIS1(a, b, c, k1):
    return 0.08 * (c + k1/2) + 0.02*( b + k1/2) - 0.03 * (a + k1/2)


def kTRES1(a, b, c, k2):
    return 0.08 * (c + k2/2) + 0.02*( b + k2/2) - 0.03 * (a + k2/2)


def kQUATRO1(a, b, c, k3):
    return 0.08 * (c + k3) + 0.02*( b + k3) - 0.03 * (a + k3)


def kUM2(a, b):
    return 0.03 * a - (0.01 + 0.02) * b


def kDOIS2(a, b, k1):
    return 0.03 * (a + k1 / 2) - (0.01 + 0.02) * (b + k1 / 2)


def kTRES2(a, b, k2):
    return 0.03 * (a + k2 / 2) - (0.01 + 0.02) * (b + k2 / 2)


def kQUATRO2(a, b, k3):
    return 0.03 * (a + k3) - (0.01 + 0.02) * (b + k3)


def kUM3(c):
    return -0.08 * c


def kDOIS3(c, k1):
    return -0.08 * (c + k1 / 2)


def kTRES3(c, k2):
    return -0.08 * (c + k2 / 2)


def kQUATRO3(c, k3):
    return -0.08 * (c + k3)


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


k31 = 0
k32 = 0
k33 = 0
k34 = 0


a = 100 
b = 10
c = 20


auxa = 0 
auxc = 0
auxb = 0


err = 500


plt.ioff()


at = []
axa = []
axb = []
axc = []


while t < 900:

    auxa = b
    auxc = a
    auxd = c


    k11 = h * kUM1(a, b,c)
    k21 = h * kUM2(a, b)


    k12 = h * kDOIS1 (a, b, c, k11)
    k22 = h * kDOIS2 (a, b, k21)


    k13 = h * kTRES1 (a, b, c, k12)
    k23 = h * kTRES2 (a, b, k22)


    k14 = h * kQUATRO1 (a, b, c, k13)
    k24 = h * kQUATRO2 (a, b, k23)


    k31 = h * kUM3 (c)
    k32 = h * kDOIS3 (c,k31)
    k33 = h * kTRES3 (c,k32)
    k34 = h * kQUATRO3 (c,k33)


    print('t:{}  a:{}  b:{}  c:{}  erro:{}'.format(t, a, b, c, err))


    at.append(t)
    axb.append(b)
    axa.append(a)
    axc.append(c)
    a = a + (k11 + 2 * k12 + 2 * k13 + k14) / 6
    b = b + (k21 + 2 * k22 + 2 * k23 + k24) / 6
    c = c + (k31 + 2 * k32 + 2 * k33 + k34) / 6
    err = (b - auxa) / auxa + (a - auxc) / auxc + (c - auxd) / auxd
    t = t + h


plt.plot(at, axa, label = 'a') #linha azul
plt.plot(at, axb, label = 'b') #linha laranja
plt.plot(at, axc, label = 'c') #linha verde 
plt.xlabel('tempo (t)')
plt.ylabel('a, b e c')
plt.title('RK4')
plt.show()