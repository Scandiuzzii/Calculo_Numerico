import matplotlib.pyplot


def condicoes_inicial(x):
    return x * (x - 1)



def TmaisUM(t, t1):
    i = 0
    while i < 11:
        if i == 10:
            t1.append (t[i] + 0.001 * (t[i - 1] - 2 * t[i] + 0))
            break
        else:
            t1.append (t[i] + 0.001 * (t[i - 1] - 2 * t[i] + t[i + 1]))
        i = i + 1


t0 = []


j = 0
while j < 110:
    t0.append(condicoes_inicial(j))
    j += 10


t1 = []
TmaisUM (t0, t1)


t2 = []
TmaisUM (t1, t2)


t3 = []
TmaisUM (t2, t3)



t4 = []
TmaisUM (t3, t4)


t5 = []
TmaisUM (t4, t5)


t6 = []
TmaisUM (t5, t6)


t7 = []
TmaisUM (t6, t7)


t8 = []
TmaisUM (t7, t8)


t9 = []
TmaisUM (t8, t9)


t10 = []
TmaisUM (t9, t10)



print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)
print(t10)



seg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 


matplotlib.pyplot.plot (seg, t0, label='T0(t)')
matplotlib.pyplot.plot (seg, t1, label='T1(t)')
matplotlib.pyplot.plot (seg, t2, label='T2(t)')
matplotlib.pyplot.plot (seg, t3, label='T3(t)')
matplotlib.pyplot.plot (seg, t4, label='T4(t)')
matplotlib.pyplot.plot (seg, t5, label='T5(t)')
matplotlib.pyplot.plot (seg, t6, label='T6(t)')
matplotlib.pyplot.plot (seg, t7, label='T7(t)')
matplotlib.pyplot.plot (seg, t8, label='T8(t)')
matplotlib.pyplot.plot (seg, t9, label='T9(t)')
matplotlib.pyplot.plot (seg, t10, label='T10(t)')
matplotlib.pyplot.xlabel ('tempo (t)')
matplotlib.pyplot.ylabel ('Temperatura (t)')
matplotlib.pyplot.legend ()
matplotlib.pyplot.show ()