'''
Programa para resolução do relatório 3 de instrumentação.
'''

# Importando bibliotecas
##################################################################
import matplotlib.pyplot as plt
import numpy as np

# Importando dados
##################################################################
seno_2kh_cf_100000 = open("./DADOS_GRUPO3_2000_cf_sen_100000.txt")
seno_2kh_sf_100000 = open("./DADOS_GRUPO3_2000_sf_sen_100000.txt")

seno_8kh_cf_10000 = open("./DADOS_GRUPO3_8000_cf_sen_10000.txt")
seno_8kh_sf_100000 = open("./DADOS_GRUPO3_8000_sf_sen_100000.txt")

seno_2kh_cf_1024 = open("./DADOS_GRUPO3_2000_cf_sen_1024.txt")
seno_2kh_sf_1024 = open("./DADOS_GRUPO3_2000_sf_sen_1024.txt")

quad_2kh_cf_1024 = open("./DADOS_GRUPO3_2000_cf_qua_1024.txt")
quad_2kh_sf_1024 = open("./DADOS_GRUPO3_2000_sf_qua_1024.txt")

quad_2kh_cf_10000 = open("./DADOS_GRUPO3_2000_cf_qua_10000.txt")
quad_2kh_sf_10000 = open("./DADOS_GRUPO3_2000_sf_qua_10000.txt")

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


seno_8kh_sf_100000_data = []
for i in seno_8kh_sf_100000.readlines():
    seno_8kh_sf_100000_data.append(float(i))


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


quad_2kh_cf_10000_data = []
for i in quad_2kh_cf_10000.readlines():
    quad_2kh_cf_10000_data.append(float(i))


quad_2kh_sf_10000_data = []
for i in quad_2kh_sf_10000.readlines():
    quad_2kh_sf_10000_data.append(float(i))

dados = [seno_2kh_cf_100000_data, seno_2kh_sf_100000_data,
         seno_8kh_cf_10000_data, seno_8kh_sf_100000_data,
         seno_2kh_cf_1024_data, seno_2kh_sf_1024_data,
         quad_2kh_cf_1024_data, quad_2kh_sf_1024_data,
         quad_2kh_cf_10000_data, quad_2kh_sf_10000_data]

dados_name = ["seno_2kh_cf_100000_data", "seno_2kh_sf_100000_data",
         "seno_8kh_cf_10000_data", "seno_8kh_sf_100000_data",
         "seno_2kh_cf_1024_data", "seno_2kh_sf_1024_data",
         "quad_2kh_cf_1024_data", "quad_2kh_sf_1024_data",
         "quad_2kh_cf_10000_data", "quad_2kh_sf_10000_data"]

# Plotando dados
##################################################################
for i, caso in enumerate(dados):
    plt.plot(caso)
    plt.title(dados_name[i])

    plt.show()
    transformada = np.fft.fft(caso)
    N = transformada.size

    f = np.fft.fftfreq(len(transformada), 20)

    frequencias = f[:N // 2]
    amplitudes = np.abs(transformada)[:N // 2] * 1 / N

    plt.bar(frequencias, amplitudes, width=0.0015)

    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Amplitude")
    plt.show()
