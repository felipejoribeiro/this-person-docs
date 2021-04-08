'''
    Lista 1 de instrumentação.

    Author: Felipe J. O. Ribeiro
'''

###############################################################################
# Modules
###############################################################################

from math import sqrt
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

###############################################################################
# Functions
###############################################################################

def my_histogram(dados, classes):
    '''
        Plota o histograma dos dados de input.
    '''
    # Plot dos dados
    dados.plot.hist(grid=True, bins=classes)
    plt.title("Histograma")
    plt.show()


def chauvenet(dados, mostrar_dados):
    '''
        Filtra os dados segundo o critério de chauvenet
    '''

    # Pegando dados estatísticos
    dados_np = np.array(dados)
    std = dados_np.std()
    mean = dados_np.mean()

    # Conseguindo valor da tabela de chauvenet
    dr_o = stats.norm.ppf(1-(1/(4*len(dados))))

    # mostra dados de forma condicional
    if mostrar_dados:
        print("DRO = ", dr_o)
        print("----------------------------")

    novos_dados = []
    for elemento in dados:

        # Calculo da dispersão para esse valor
        dr_x = abs(elemento - mean)/std

        # Checando conformidade
        if dr_x < dr_o:
            if mostrar_dados:
                print("{} --> atende".format(elemento))
            novos_dados.append(elemento)
        else:
            if mostrar_dados:
                print("{} --> não atende".format(elemento))
    if mostrar_dados:
        print("----------------------------")
        print("Valor médio : {}".format(np.mean(novos_dados)))
        print("Desvio padrão : {:.3f}".format(np.std(novos_dados)))

    return novos_dados


def teste_qui_quadrado(dados, classes, media, std, plotar):
    '''
        Realisa o teste do qui-quadrado nos dados de entrada
    '''
    # Quantidade de valores
    x_n = len(dados)

    # Valores estatísticos
    mean = media
    sig_x = std

    # Monta-se o histograma, se consegue os integrantes e os limites
    n_o, lik= np.histogram(dados, classes)

    # Achan-se os valores esperados para a distribuição
    n_e = []
    n_e.append(stats.norm.cdf(lik[1], mean, sig_x)*x_n
               - stats.norm.cdf(lik[0], mean, sig_x)*x_n)
    for i in range(2, len(lik)):
        n_e.append((stats.norm.cdf(lik[i], mean, sig_x)
                   - stats.norm.cdf(lik[i - 1], mean, sig_x) )*x_n)

    # Achando as diferenças normalizadas
    soma = 0
    soma_i = []
    for i, n_ol in enumerate(n_o):
        soma = soma + ((n_e[i] - n_ol)**2)/n_e[i]
        soma_i.append(((n_e[i] - n_ol)**2)/n_e[i])

    # print(soma)
    # Número de parâmetros da gaussiana
    n_p = 2

    # graus de liberdade
    g_l = classes - 1 - n_p

    # cálculo da confiança
    alpha = 1 - stats.chi2.cdf(soma, g_l)


    if plotar:
        # Amostra no console
        for i, elemento in enumerate(n_o):
            print(elemento, n_e[i], soma_i[i])

        # Mostra resultado
        print ("alpha = ", alpha)
        # Amostra gráfica
        plt.plot(n_e, label="esperado")
        plt.plot(n_o, label="adquirido")
        plt.legend()
        plt.show()







###############################################################################
# Main Routine
###############################################################################

if __name__ == "__main__":

    ## Teste
    dado_teste = [10.02, 10.2, 10.26, 10.2, 10.22, 10.13, 9.97, 10.12, 10.09,
                  9.9, 10.05, 10.17, 10.42, 10.21, 10.23, 10.11, 9.98, 10.1,
                  10.04, 9.81]
    # teste_qui_quadrado(dado_teste, 6, np.mean(dado_teste), 0.138, True)

    ## Questão 1
    # Dados da primeira questão
    DATA=[28.68, 28.66, 28.70, 28.57, 28.61, 28.59, 28.71, 28.59, 28.69, 28.58,
          28.73, 28.55, 28.71, 28.70, 28.57, 28.56, 28.58, 28.50, 28.68, 28.69]

    # Declarando uma série pandas
    DATA_PD = pd.Series(DATA)

    # Plota os dados
    # my_histogram(DATA_PD, 5)

    ## Questão 2 e 3
    # Dados da segunda questão
    VALOR_MEDIO = 28.58
    ALPHA = 0.10
    IC_ALPHA = 0.95

    # Procura-se na tabela pra achar o valor Z_theta para o IC_ALPHA
    BETHA = (1 + 0.95)/2  # 0.975 -> tabela -> 1.96
    Z = 1.96

    D = (2.093 * 0.066923)/sqrt(20)
    D1 = 28.6325 + D
    D2 = 28.6325 - D
    # print(D, D2, D1)

    ## Questão 3
    # Para achar o valor médio
    MEAN_X = np.mean(DATA)
    STAND_DEV_X = np.std(DATA)

    # Questão 4

    DATA_4 = [5.42, 5.71, 5.82, 5.45, 5.87, 5.40, 5.73, 5.64, 5.83, 5.75]
    chauvenet(DATA_4, False)

    # Questão 5
    chauvenet(DATA, False)

    # Questão 6
    teste_qui_quadrado(DATA_4, 5, 5.8, 0.8, True)

    # Experimento
dados = [21.000000, 22.000000, 21.000000, 21.000000, 22.000000, 21.000000,
         21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000,
         21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000,
         21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000,
         21.000000, 22.000000, 21.000000, 22.000000, 21.000000, 21.000000,
         22.000000, 21.000000, 22.000000, 21.000000, 22.000000, 21.000000,
         22.000000, 21.000000, 21.000000, 21.000000, 21.000000, 22.000000,
 21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 22.000000,
 21.000000, 21.000000, 22.000000, 22.000000, 21.000000, 21.000000, 22.000000,
 21.000000, 22.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000,
 21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000,
 22.000000, 22.000000, 21.000000, 21.000000, 21.000000, 22.000000, 21.000000,
 21.000000, 22.000000, 21.000000, 21.000000, 21.000000, 21.000000, 21.000000,
 21.000000, 22.000000, 21.000000, 21.000000, 21.000000, 22.000000, 21.000000,
 21.000000, 22.000000, 21.000000, 22.000000, 21.000000, 22.000000, 21.000000,
 22.000000, 21.000000]

# teste_qui_quadrado(dados,12, np.mean(dados), np.std(dados),True)
