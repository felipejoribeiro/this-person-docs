'''
Programa para resolução do relatório 3 de instrumentação.
'''

# Importando bibliotecas
##################################################################
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fft import fft,fftfreq
import scipy.fftpack

# Importando dados
##################################################################
seno_2kh_cf_100000 = open("./DADOS_GRUPO3_2000_cf_sen_100000.txt")
seno_2kh_sf_100000 = open("./DADOS_GRUPO3_2000_sf_sen_100000.txt")

seno_8kh_cf_10000 = open("./DADOS_GRUPO3_8000_cf_sen_10000.txt")
seno_8kh_sf_10000 = open("./DADOS_GRUPO3_8000_sf_sen_10000.txt")

seno_2kh_cf_1024 = open("./DADOS_GRUPO3_2000_cf_sen_1024.txt")
seno_2kh_sf_1024 = open("./DADOS_GRUPO3_2000_sf_sen_1024.txt")

quad_2kh_cf_1024 = open("./DADOS_GRUPO3_2000_cf_qua_1024.txt")
quad_2kh_sf_1024 = open("./DADOS_GRUPO3_2000_sf_qua_1024.txt")

quad_2kh_cf_1000 = open("./DADOS_GRUPO3_2000_cf_qua_1000.txt")
quad_2kh_sf_1000 = open("./DADOS_GRUPO3_2000_sf_qua_1000.txt")

# Criando estrutura de dados
##################################################################
seno_2kh_cf_100000_data = []
for i in seno_2kh_cf_100000.readlines():
    seno_2kh_cf_100000_data.append(float(i))


seno_2kh_sf_100000_data = []
for i in seno_2kh_sf_100000.readlines():
    seno_2kh_sf_100000_data.append(float(i))


seno_8kh_cf_10000_data = []
for i in seno_8kh_cf_10000.readlines():
    seno_8kh_cf_10000_data.append(float(i))


seno_8kh_sf_10000_data = []
for i in seno_8kh_sf_10000.readlines():
    seno_8kh_sf_10000_data.append(float(i))


seno_2kh_cf_1024_data = []
for i in seno_2kh_cf_1024.readlines():
    seno_2kh_cf_1024_data.append(float(i))


seno_2kh_sf_1024_data = []
for i in seno_2kh_sf_1024.readlines():
    seno_2kh_sf_1024_data.append(float(i))


quad_2kh_cf_1024_data = []
for i in quad_2kh_cf_1024.readlines():
    quad_2kh_cf_1024_data.append(float(i))


quad_2kh_sf_1024_data = []
for i in quad_2kh_sf_1024.readlines():
    quad_2kh_sf_1024_data.append(float(i))


quad_2kh_cf_1000_data = []
for i in quad_2kh_cf_1000.readlines():
    quad_2kh_cf_1000_data.append(float(i))


quad_2kh_sf_1000_data = []
for i in quad_2kh_sf_1000.readlines():
    quad_2kh_sf_1000_data.append(float(i))

dados = [seno_2kh_cf_100000_data, seno_2kh_sf_100000_data,
         seno_8kh_cf_10000_data, seno_8kh_sf_10000_data,
         seno_2kh_cf_1024_data, seno_2kh_sf_1024_data,
         quad_2kh_cf_1024_data, quad_2kh_sf_1024_data,
         quad_2kh_cf_1000_data, quad_2kh_sf_1000_data]

dados_name = ["seno_2kh_cf_100000_data", "seno_2kh_sf_100000_data",
         "seno_8kh_cf_10000_data", "seno_8kh_sf_10000_data",
         "seno_2kh_cf_1024_data", "seno_2kh_sf_1024_data",
         "quad_2kh_cf_1024_data", "quad_2kh_sf_1024_data",
         "quad_2kh_cf_1000_data", "quad_2kh_sf_1000_data"]

dados_2 = [[seno_2kh_cf_100000_data, seno_2kh_sf_100000_data],
                [seno_8kh_cf_10000_data, seno_8kh_sf_10000_data],
                [seno_2kh_cf_1024_data, seno_2kh_sf_1024_data],
                [quad_2kh_cf_1024_data, quad_2kh_sf_1024_data],
                [quad_2kh_cf_1000_data, quad_2kh_sf_1000_data]]

dados_name_2 = ["seno_2kh_100000_data",
                 "seno_8kh_10000_data",
                 "seno_2kh_1024_data",
                 "quad_2kh_1024_data",
                 "quad_2kh_1000_data"]





# Plotando dados
##################################################################
for i, caso in enumerate(dados):

    print(dados_name[i], len(caso))

    N = len(caso)

    T = 1/(10 * 10**3)

    dados_teste_x = np.linspace(0, N * T, N)
    dados_teste_y = caso

    yf = scipy.fftpack.fft(dados_teste_y)
    xf = np.linspace(0.0, 1.0//(T),N)

    plt.plot(xf,np.abs(yf) * 2.0/N)
    plt.grid()
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Amplitude")
    plt.title(dados_name[i])

    plt.savefig(dados_name[i] + ".png")

    plt.close()


for i, caso in enumerate(dados_2):

    print(dados_name_2[i], len(caso[0]))

    N = len(caso[0])

    T = 1/(10 * 10**3)

    dados_teste_x = np.linspace(0, N * T, N)
    dados_teste_y = caso[0]
    dados_teste_y_2 = caso[1]

    yf = scipy.fftpack.fft(dados_teste_y)
    yf_2 = scipy.fftpack.fft(dados_teste_y_2)
    xf = np.linspace(0.0, 1.0//(T),N)

    plt.plot(xf,np.abs(yf) * 2.0/N, label="com friltro")
    plt.plot(xf,np.abs(yf_2) * 2.0/N, label="Sem filtro")
    plt.grid()
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.title(dados_name_2[i])
    # plt.show()
    plt.savefig(dados_name_2[i] + ".png")
    plt.close()