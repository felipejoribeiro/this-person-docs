# Segunda feira

    Instrumentação                  07:10 - 09:40
    Eletrônica de aeronaves         10:40 - 12:20
    Instrumentação                  13:10 - 14:10

# Terça feira
    
    Eletrônica de aeronaves         07:10 - 08:50
    Sistemas de aeronaves           08:50 - 10:40
    Transferência de calor 2        10:40 - 12:20

# Quarta feira
    
    Aerodinâmica alicada            08:50 - 10:40

# Quinta feira 

    Transferência de calor 2(async) 07:10 - 08:50
    Sistemas de aeronaves           09:50 - 11:30
    Aerodinâmica aplicada           13:10 - 14:50

# Sexta feira

    Aerodinâmica aplicada           08:00 - 08:50


-----------------------------------------------------

# Avisos
- Pesquisar formas de deixar o modelo mais rápido.
- Estudar transistors de eletrônica de aeronaves, uma vez que o assunto está um pouco nebuloso.
- Iniciar procura de emprego no Canadá.

- Nome do arquivo de prova deve ser número de matrícula na prova de eletrônica.
- para o trabalho de instrumentação: https://www.youtube.com/watch?v=hjmM7wRGMPE
- 

#########################################################################################################
# APLICA A FUNÇÃO PREDICT (TANTO NO CONJUNTO DE DADOS DE TREINAMENTO QUANTO NO CONJUNTO DE DADOS DE TESTE)
train_predict = y_scaler.inverse_transform(moe.predict_values(np.c_[x_train_serie]))
teste_predict = y_scaler.inverse_transform(moe.predict_values(np.c_[x_teste_serie]))
#########################################################################################################
##############################################################################################
# DEFINE UM ESCALADOR PARA A NORMALIZAÇÃO DOS DADOS
x_scaler = MinMaxScaler() # APLICA UM NORMALIZAÇÃO DOS DADOS 
y_scaler = MinMaxScaler() # APLICA UM NORMALIZAÇÃO DOS DADOS 
x_scaler = x_scaler.fit(x_train_serie)
y_scaler = y_scaler.fit(y_train_serie)
########################################################################################
-----------------------------------------------------
# TODO (22/04)
[-]Instrumentação - Ver aula assíncrona (2) [][].
[x]aerodinâmica - Fazer questão da lista de aerodinâmica.
[-]TC2 - ver aula assíncrona 8. -> https://youtu.be/O7tKbDqGnLc
[-]TC2 - ver aula assíncrona 9. -> https://youtu.be/O7tKbDqGnLc

-----------------------------------------------------
# TODO (22/04)
[-]Instrumentação - Ver aula assíncrona (2) [][].
[x]aerodinâmica - Fazer questão da lista de aerodinâmica.
[-]TC2 - ver aula assíncrona 8. -> https://youtu.be/O7tKbDqGnLc
[-]TC2 - ver aula assíncrona 9. -> https://youtu.be/O7tKbDqGnLc

-----------------------------------------------------
# TODO (20/04)
[x]Reunião do mflab.
[-]Instrumentação - Ver aula assíncrona (2) [][].
[x]aerodinâmica - Começar a lista de aerodinâmica.
[-]TC2 - ver aula assíncrona 8. -> https://youtu.be/O7tKbDqGnLc

# TODO (06/04)
[-]Instrumentação - Ver aula assíncrona (2) [][].
[x]Eletrônica -  fazer trabalho.
[-]aerodinâmica - Começar a lista de aerodinâmica.
[-]TC2 - ver aula assíncrona 8. -> https://youtu.be/O7tKbDqGnLc
[x]Reunião do mflab.

# TODO (05/04)
- Foi passada a lista três de instrumentação.
- Prova dia 19. Uma questão pra aula toda.
- Diminui pra 10000 o senoide sem filtro.
- Diminui o quadrado (não da de comparar a amplitude direito. Só analisa 1000 pontos da quadrada e 10000 do 8k. Usar o filtro pra distinguir sinal fantasma.)
- Prova eletrotécnica: lista exercício manuscrita em relatório semana que vem. Capa: nome, número, avaliação número 1. Não pode copiar a lista do colega. Precisa fazer a mão as questões(papel).

[-]Instrumentação - Ver aula assíncrona (2) [][].
[-]aerodinâmica - Começar a lista de aerodinâmica.

# TODO (28/03)
[-]Instrumentação - Ver aula assíncrona (2) [][].
[x]Instrumentação - Fazer questões lista (2) [][].
[x]Instrumentação - Ler e processar material do relatório.
[-]aerodinâmica - Começar a lista de aerodinâmica.

# TODO (25/03)
[-]Instrumentação - Ver aula assíncrona (2) [][].
[-]Instrumentação - Fazer questões lista (2) [][].
[-]Instrumentação - Ler e processar material do relatório.
[-]aerodinâmica - Começar a lista de aerodinâmica.

# TODO (23/03)
[x]TC2 - Ver aula assíncrona 7. -> https://youtu.be/RG6aMIHLrMU
[x]TC2 - Ver aula síncrona segunda -> baixar meets as tarefas resolvidas.
[-]Instrumentação - Ver aula assíncrona (2) [][].
[-]Instrumentação - Fazer questões lista (2) [][].
[-]Instrumentação - Ler e processar material do relatório.
[-]aerodinâmica - Começar a lista de aerodinâmica.

# TODO (23/03)
[x]TC2 - Ver aula assíncrona 4. -> https://youtu.be/9AOTLIBgxzM
[x]TC2 - Ver aula assíncrona 5. -> https://youtu.be/-clrULsTJQk
[x]TC2 - Ver aula assíncrona 6. -> https://youtu.be/Yk4m8yMNQwI
[-]TC2 - Ver aula assíncrona 7. -> https://youtu.be/RG6aMIHLrMU

# TODO (22/03)
[x]Lab - reunião Tatiane (16)
[-]Eletrônica - Fazer anotações da aula de segunda.
[-]Eletrônica - Fazer anotações da aula de terça.
[-]TC2 - Ver aula assíncrona 4. -> https://youtu.be/9AOTLIBgxzM
[-]TC2 - Ver aula assíncrona 5. -> https://youtu.be/-clrULsTJQk
[-]TC2 - Ver aula assíncrona 6. -> https://youtu.be/Yk4m8yMNQwI

# TODO (18/03)
[-]Eletrônica - Fazer anotações da aula de segunda.
[-]Eletrônica - Fazer anotações da aula de terça.
[-]TC2 - Ver aula assíncrona 4. -> https://youtu.be/9AOTLIBgxzM
[-]TC2 - Ver aula assíncrona 5. -> https://youtu.be/-clrULsTJQk
[-]TC2 - Ver aula assíncrona 6. -> https://youtu.be/Yk4m8yMNQwI
[x][x][x][x][x][x][x]Aerodinâmica - 7 exercícios --> lista terminada

# TODO (17/03)
[x]Lab - revisar apresentação pesquisa.
[-]Eletrônica - Fazer anotações da aula de segunda.
[-]Eletrônica - Fazer anotações da aula de terça.
[-]TC2 - Ver aula assíncrona 4. -> https://youtu.be/9AOTLIBgxzM
[-]TC2 - Ver aula assíncrona 5. -> https://youtu.be/-clrULsTJQk
[-]TC2 - Ver aula assíncrona 6. -> https://youtu.be/Yk4m8yMNQwI
[x][x][x][x][x][x][x]Aerodinâmica - 7 exercícios

# TODO (16/03)
[x]Lab - Concluir apresentação pesquisa.
[-]Lab - revisar apresentação pesquisa.
[-]Eletrônica - Fazer anotações da aula de segunda.
[-]Eletrônica - Fazer anotações da aula de terça.
[-]TC2 - Ver aula assíncrona 4. -> https://youtu.be/9AOTLIBgxzM
[-]TC2 - Ver aula assíncrona 5. -> https://youtu.be/-clrULsTJQk
[-]TC2 - Ver aula assíncrona 6. -> https://youtu.be/Yk4m8yMNQwI

# TODO (15/03)
- Houve aula de laboratório instrumentação: para entregar 29.
[x]Lab - Dar andamento apresentação pesquisa.
[x]Lab - Gerar resultados para apresentação do lab.
[-]TC2 - Ver aula assíncrona 4. -> https://youtu.be/9AOTLIBgxzM
[-]TC2 - Ver aula assíncrona 5. -> https://youtu.be/-clrULsTJQk
[-]TC2 - Ver aula assíncrona 6. -> https://youtu.be/Yk4m8yMNQwI

# TODO (14/03)

[x]Instrumentação - Fazer lista de exercícios de número 1.
[x]Instrumentação - fazer relatório do laboratório 1.
[-]Lab - Dar andamento apresentação pesquisa.

# TODO (11/03)

[x]Instrumentação - Ver aula base estatística e fazer anotação dela.
[-]Instrumentação - Aplicar os estudos as dados do laboratório 1.
[-]Instrumentação - fazer relatório do laboratório 1.
[x]Home - participar competição programação.
[-]Lab - Dar andamento apresentação pesquisa.

# TODO (10/03)

[x]Home - Organizar fotos HD.
[-]Instrumentação - Ver aula base estatística e fazer anotação dela.
[-]Instrumentação - Fazer lista de exercícios de número 1.
[-]Instrumentação - fazer relatório do laboratório 1.

# TODO (09/03)

[-]Instrumentação - Ver aula base estatística e fazer anotação dela.
[-]Instrumentação - Fazer lista de exercícios de número 1.
[-]Instrumentação - fazer relatório do laboratório 1.
[x]TC2 - ver aula 1 assíncrona e fazer anotações.
[x]TC2 - ver aula 2 assíncrona e fazer anotações.
[x]TC2 - ver aula 3 assíncrona e fazer anotações.
[x]Eletrônica - completar anotações da aula de terça.
[x]Eletrônica - completar anotações da aula de segunda.
[x]Eletrônica - baixar livro do malvino (checar no plano de ensino).
