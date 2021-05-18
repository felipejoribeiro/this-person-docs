"""
Programa para printar os dados dos experimentos de instrumentação.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.fftpack

def no_tempo(caso, nome):
    N = len(caso)

    T = 1/(1 * 10**2)
    
    x = []
    for i in range(N):
        x.append(i * T)

    plt.plot(x,caso)
    plt.grid()
    plt.xlabel("Tempo (s)")
    plt.ylabel("Voltagem")
    plt.title(nome)
    plt.show()

    plt.savefig("dados_tempo_" + nome + ".png")
    plt.close()

def transformada(caso, nome):
    N = len(caso)

    T = 1/(1 * 10**2)

    dados_teste_y = caso

    yf = scipy.fftpack.fft(dados_teste_y)
    xf = np.linspace(0.0, 1.0//(T),N)

    plt.plot(xf,np.abs(yf) * 2.0/N)
    plt.grid()
    plt.xlim([-1,50])
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Amplitude")
    plt.title(nome)
    plt.show()

    plt.savefig("dados" + ".png")
    plt.close()

aquecimento = open("./TemperaturaG3.txt")
resfriamento = open("./Temperatura_DescidaG3.txt")

aquecimento_data = []
for i in aquecimento.readlines():
    aquecimento_data.append(float(i))

resfriamento_data = []
for i in resfriamento.readlines():
    resfriamento_data.append(float(i))

print(len(aquecimento_data))

transformada(aquecimento_data, "Aquecimento_data")
transformada(resfriamento_data, "Resfriamento_data")
no_tempo(aquecimento_data, "Aquecimento_data")
no_tempo(resfriamento_data, "Resfriamento_data")

