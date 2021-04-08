'''
Programa para a solução da lista 2 de instrumentação.

'''

import math as mt
import matplotlib.pyplot as plt
import numpy as np

# General application functions
###############################################################################
def less_square_linear_reduction(vector_x, vector_y, show_graph):
    '''
    Executa a regreção linear em mínimos quadrados dos dois vetores de entrada
    '''

    # Initializing some local variables
    x_sum = 0
    y_sum = 0
    square_x_sum = 0
    square_y_sum = 0
    x_prod = 1
    y_prod = 1
    cros_prod_sum = 0
    length = len(vector_x)

    # Checking length from both input vectors
    if len(vector_y) != length :
        print("[ERROR] - Vectors must have same length")
        return

    # Calculating some usefull measures
    for i in enumerate(vector_x):
        x_sum += vector_x[i[0]]
        y_sum += vector_y[i[0]]
        square_x_sum += vector_x[i[0]]**2
        square_y_sum += vector_y[i[0]]**2
        x_prod = x_prod * vector_x[i[0]]
        y_prod = y_prod * vector_y[i[0]]
        cros_prod_sum += vector_x[i[0]] * vector_y[i[0]]

    # Determining angular and scallar constants for the linear regression.
    a_constant = (length * cros_prod_sum - x_sum * y_sum)/(length * square_x_sum -
                                                  x_sum**2)
    b_constant = (y_sum * square_x_sum - cros_prod_sum * x_sum)/(length * square_x_sum -
                                                        x_sum**2)

    # Generating graph of the linear regression
    x_result = np.linspace(vector_x[0], vector_x[length - 1], 100)
    y_result = a_constant * x_result + b_constant

    # calculating losses
    losses = [vector_y[i] - (a_constant * vector_x[i] + b_constant) for i
              in range(length)]

    # Ploting results if convenient
    if show_graph:
        plt.figure()
        plt.subplot(211)
        plt.plot(x_result, y_result, label ="Regressão linear")
        plt.scatter(vector_x, vector_y, c="black", label = "Dados de entrada",
                    zorder=10)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.subplot(212)
        plt.plot([vector_x[0], vector_x[len(vector_x) - 1]], [0, 0], c="black",
                 zorder = -1)
        plt.bar(vector_x, losses, width=2, color="red")
        plt.scatter(vector_x, losses, c="red")
        plt.xlabel("x")
        plt.ylabel("Desvio")
        plt.show()
        print("Linear regrecion ==> f(x) = {:.3f} x + {:.3f}".format(a_constant, b_constant))
    return a_constant, b_constant, losses



# Exercise functions
###############################################################################
def questao_1_a():
    '''
    Primeira questão - a
    '''
    data_x = [120, 90, 60, 30, 0, -30, -60, -90, -120]
    data_y = [0.99, 0.92, 0.79, 0.67, 0.51, 0.38, 0.21, 0.088, 0.018]

    print("Primeira questão")

    # Call of the regretion function as defined in the question
    less_square_linear_reduction(data_x, data_y, True)


def questao_1_b():
    '''
    Primeira questão - b
    '''
    data_x = [120, 90, 60, 30, 0, -30, -60, -90, -120]
    data_y = [0.99, 0.92, 0.79, 0.67, 0.51, 0.38, 0.21, 0.088, 0.018]

    print("primera questão - b")

    _, _, loss_fit = less_square_linear_reduction(data_x, data_y, False)

    print("Calculando o desvio padrão da reta")

    loss_fit_sum = 0
    for element in loss_fit:
        loss_fit_sum += element**2

    # Por ser um fit linear (n - 1 - p) com p = 1:
    v_fit = len(loss_fit) - 2

    s_fit = mt.sqrt(loss_fit_sum/v_fit)


    print("Achar t student, com alpha = 95% e t = 9 ==> 2.365")

    t_stu = 2.365


    d_y = t_stu * s_fit/mt.sqrt(len(loss_fit))

    # Calculando y médio
    y_med = np.array(data_y).mean()
    print(s_fit)
    print(d_y)
    print(y_med)
    print(s_fit)

    print("Assim, temos um intervalo de confiança de:")

    print("{:.3f} <= y <= {:.3f}".format(y_med - d_y, y_med + d_y))


def questao_1_c():
    '''
    Primeira questão - c
    '''
    print("primeira questão - c")
    novo_y = ( 0.62 - 0.508 )/( 0.004 )
    print(novo_y)


def questao_1_d():
    '''
    Primeira questão - d
    '''
    data_x = [120, 90, 60, 30, 0, -30, -60, -90, -120]
    data_y = [0.99, 0.92, 0.79, 0.67, 0.51, 0.38, 0.21, 0.088, 0.018]

    a_fit, b_fit, loss_fit = less_square_linear_reduction(data_x, data_y, False)

    print("primeira questão - d")

    loss_fit_sum = 0
    for element in loss_fit:
        loss_fit_sum += element**2
    v_fit = len(loss_fit) - 2
    s_fit = mt.sqrt(loss_fit_sum/v_fit)
    t_stu = 2.262
    d_y = t_stu * s_fit/mt.sqrt(len(loss_fit))

    # Initializing some local variables
    x_sum = 0
    y_sum = 0
    square_x_sum = 0
    square_y_sum = 0
    x_prod = 1
    y_prod = 1
    cros_prod_sum = 0
    n_data = len(data_x)

    # Calculating some usefull measures
    for i in enumerate(data_x):
        x_sum += data_x[i[0]]
        y_sum += data_y[i[0]]
        square_x_sum += data_x[i[0]]**2
        square_y_sum += data_y[i[0]]**2
        x_prod = x_prod * data_x[i[0]]
        y_prod = y_prod * data_y[i[0]]
        cros_prod_sum += data_x[i[0]] * data_y[i[0]]

    s_a = mt.sqrt(n_data * s_fit**2/(n_data * square_x_sum - x_sum**2))
    s_b = mt.sqrt((s_fit**2)*square_x_sum /(n_data * square_x_sum - (x_sum)**2) )

    d_a = t_stu * s_a/mt.sqrt(len(loss_fit))
    d_b = t_stu * s_b/mt.sqrt(len(loss_fit))

    y_case = 0.62

    d_result = t_stu * mt.sqrt((d_y/a_fit)**2 + (d_b/a_fit)**2 +
                               (d_a * (b_fit - y_case)/(a_fit**2))**2)

    print(d_result) # 12,817732


def questao_1_e():
    '''
    Primeira questão - e
    '''
    data_x = [120, 90, 60, 30, 0, -30, -60, -90, -120]
    data_y = [0.99, 0.92, 0.79, 0.67, 0.51, 0.38, 0.21, 0.088, 0.018]

    a_fit, _, loss_fit =less_square_linear_reduction(data_x, data_y, False)


    print("primeira questão - e")
    max_loss = np.array(loss_fit).max()

    FS = 120

    Li = max_loss/FS
    print (Li)
    print(10 * a_fit)


# Main call
###############################################################################
if __name__ == "__main__":
    questao_1_a()
    questao_1_b()
    questao_1_c()
    questao_1_d()
    questao_1_e()

    # Laboratório

    # Data input
    DATA_10 = []
    with open("./../lab_2/G3_11.txt") as file:
        content = file.readlines()
        for line in content:
            DATA_10.append(float(line))
    DATA_20 = []
    with open("./../lab_2/G3_20.txt") as file:
        content = file.readlines()
        for line in content:
            DATA_20.append(float(line))
    DATA_30 = []
    with open("./../lab_2/G3_30.txt") as file:
        content = file.readlines()
        for line in content:
            DATA_30.append(float(line))

    # Data statistical results:
    data_x = [11, 20, 30]
    data_y = [12.1624, 21.9345, 32.3169]

    a, b, loss = less_square_linear_reduction(data_x, data_y, True)

    rangee = data_y[2] - data_y[0]

    print(rangee)

    maximo = np.array(loss).max()

    print(maximo)

    print(maximo/rangee)
