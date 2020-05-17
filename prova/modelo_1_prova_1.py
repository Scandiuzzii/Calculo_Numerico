import csv
import os
import matplotlib.pyplot
import requests


def baixar_arquivo(url, endereco):
    response = requests.get (url, stream = True)
    if response.status_code == requests.codes.OK:
        with open (endereco + os.path.basename (url.split ("?")[0]), 'wb') as novo_arquivo:
                for parte in response.iter_content (chunk_size = 256):
                    novo_arquivo.write(parte)
        print ("Dowloand Concluido!". format(endereco))
    
    else:
        response.raise_for_status()


def deltaX(x):
    return int (x [len (x) - 1]) - int (x [len (x) - 2])


def abrirArquivo(path):
    with open(path,'r') as confirmed:
        leitor = csv.DictReader (confirmed,delimiter =',')
        for coluna in leitor:
            if coluna['Country/Region'] == 'Brazil':
                coluna3 = coluna.values()
    x=[]
    
    
    for e in coluna3:
        x.append(e)
    return x


def kUM1(x1, x4):
    return k11 * x4 - (k31 + k21) * x1


def kDOIS1(x1, x4, k1):
    return k11 * (x4 + k1 / 2) - (k31 + k21) * (x1 + k1 / 2)


def kTRES1(x1, x4, k2):
    return k11 * (x4+k2 / 2) - (k31 + k21) * (x1 + k2 / 2)


def kQUATRO1(x1, x4, k3):
    return k11 * (x4 + k3) - (k31 + k21) * (x1 + k3)


def kUM2(x1):
    return k31 * x1


def kDOIS2(x1, k1):
    return k31 * (x1 + k1 / 2)


def kTRES2(x1, k2):
    return k31 * (x1 + k2 / 2)


def kQUATRO2(x1, k3):
    return k31 * (x1 + k3)


def kUM3(x1):
    return k21 * x1


def kDOIS3(x1, k1):
    return k21 * (x1 + k1 / 2)


def kTRES3(x1, k2):
    return k21 * (x1 + k2 / 2)


def kQUATRO3(x1, k3):
    return k21 * (x1 + k3)


def kUM4(x4):
    return -1 * k11 * x4


def kDOIS4(x4, k1):
    return -1 * k11 * (x4 + k1 / 2)



def kTRES4(x4, k2):
    return -1 * k11 * (x4 + k2 / 2)



def kQUATRO4(x4, k3):
    return -1 * k11 * (x4 + k3)



url=["https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"]


for i in range(0,3):
    baixar_arquivo(url[i],'dados/')
    
    
dados_de_confirmados = 'dados/time_series_covid19_confirmed_global.csv'
dados_de_morte = 'dados/time_series_covid19_deaths_global.csv'
dados_de_sobreviventes = 'dados/time_series_covid19_recovered_global.csv'


CASOS_confirmados = abrirArquivo (dados_de_confirmados)
CASOS_mortes = abrirArquivo (dados_de_morte)
CASOS_sobreviventes = abrirArquivo (dados_de_sobreviventes)


CASOS = 209000000 * 0.7 - int (CASOS_confirmados [ len (CASOS_confirmados) - 1])


k11 = deltaX(CASOS_confirmados) / CASOS
k31 = deltaX(CASOS_mortes) / int(CASOS_confirmados[len(CASOS_confirmados) - 2])
k21 = deltaX(CASOS_sobreviventes) / int(CASOS_confirmados[len(CASOS_confirmados) - 2])


h = 1
t = 0


rk11 = 0
rk12 = 0
rk13 = 0
rk14 = 0


rk21 = 0
rk22 = 0
rk23 = 0
rk24 = 0


rk31 = 0
rk32 = 0
rk33 = 0
rk34 = 0


rk41 = 0
rk42 = 0
rk43 = 0
rk44 = 0


x1 = int (CASOS_confirmados [ len (CASOS_confirmados) - 1])
x2 = int (CASOS_mortes [ len (CASOS_mortes) - 1])
x3 = int (CASOS_sobreviventes [ len (CASOS_sobreviventes) - 1])
x4 = CASOS


axX1 = 0
axX2 = 0
axX3 = 0
axX4 = 0


err = 0


matplotlib.pyplot.ioff()
graphT = []
graphX2 = []
graphX3 = []
graphX4 = []


while t < 100:
    axX1 = x1
    axX2 = x2
    axX3 = x3
    axX4 = x4


    rk11 = h * kUM1 (x1, x4)
    rk21 = h * kUM2 (x1)
    rk31 = h * kUM3 (x1)
    rk41 = h * kUM4 (x4)


    rk12 = h * kDOIS1 (x1, x4, rk11)
    rk22 = h * kDOIS2 (x1, rk21)
    rk32 = h * kDOIS3 (x3, rk31)
    rk42 = h * kDOIS4 (x4, rk41)


    rk13 = h * kTRES1 (x1, x4, rk12)
    rk23 = h * kTRES2 (x1, rk22)
    rk33 = h * kTRES3 (x3, rk32)
    rk43 = h * kTRES4 (x4, rk42)


    rk14 = h * kQUATRO1 (x1 ,x4, rk13)
    rk24 = h * kQUATRO2 (x1, rk23)
    rk34 = h * kQUATRO3 (x3, rk33)
    rk44 = h * kQUATRO4 (x4, rk43)


    print(f'tempo: {t} || PP: {x1:.0f} || C:{x2:.0f} || M:{x3:.0f} || R:{x4:.0f}')


    graphT.append (t)
    graphX2.append (x1)
    graphX3.append (x2)
    graphX4.append (x3)


    x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14) / 6
    x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24) / 6
    x3 = x3 + (rk31 + 2 * rk32 + 2 * rk33 + rk34) / 6
    x4 = x4 + (rk41 + 2 * rk42 + 2 * rk43 + rk44) / 6


    k11 = (x1 - axX1) / x4
    k31 = (x2 - axX2) / axX1
    k21 = (x3 - axX3) / axX1


  
    err = (x1 - axX1) / axX1 + (x2 - axX2) / axX2 + (x3 - axX3) / axX3 + (x4 - axX4) / axX4
    
    
    t = t + h


matplotlib.pyplot.plot (graphT,graphX2,label ='Casos(t)')
matplotlib.pyplot.plot (graphT,graphX3,label ='Mortes(t)')
matplotlib.pyplot.plot (graphT,graphX4,label ='Sobreviventes(t)')
matplotlib.pyplot.xlabel ('tempo (t)')
matplotlib.pyplot.ylabel ('valores (C(t) e M(t) e R(t))')
matplotlib.pyplot.legend()
matplotlib.pyplot.title('Modelo 1 - Prova 1')
matplotlib.pyplot.show()
