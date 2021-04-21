# Questão 2
Para uma amostragem de sinal, após a coleta de 10000 pontos a 10 KHz, obteve-se uma frequência de 300 Hz com amplitude de 2,5 V e uma frequência de 1230 Hz com amplitude 2,1 V, sem identificação de qualquer tipo de vazamento nas frequências. Repetindo a coleta, agora aplicando um filtro passa baixa de 2ª. ordem com frequência de corte em 5000Hz e ganho 1,01; a resposta em frequência apresentou a frequência de 300 Hz com amplitude de 2,5 V e a frequência de 1230 Hz com amplitude 1,1 V, sem vazamentos.

Sobre os dados coletados, temos:
- Amostragem de 10 KHz.
- Foram recolhidos 10000 pontos.

- Sem filtro:
    - 300 Hz (A = 2,5V) (Sem vazamento).
    - 1230 Hz (A = 2,1V) (Sem vazamento).

- Com filtro em (5000Hz) e ganho de 1,01:
    - 300 Hz (A = 2,5V) (Sem vazamento).
    - 1230 Hz (A = 1,1V) (Sem vazamento).


##### a) Qual dessas frequências obtidas é uma frequência fantasma? Justifique. (5 pontos)
A frequência fantasma encontrase em 1230 Hz, uma vez que sua amplitude diminuiu com a utilização do filtro de passa baixa.

##### b) Se a frequência de amostragem alterar-se para 2000Hz e mantiver o número de pontos coletados, qual deverá a mudança na discretização da frequência (df) após a transformada de Fourier? (5 pontos)
Calculando-se o $df$ para os dois casos de discretização, temos:

- $df_1 = \frac{10000}{10000} = 1$Hz

- $df_2 = \frac{2000}{10000} = 0,2$Hz

##### c) Se o número de amostras for alterado para 50 com frequência de coleta de 1KHz, qual(is) da(s) frequência(s) apresentaria(m) erro de vazamento? Justifique. (5 pontos)
Calculando o novo $df$ obtemos:

- $df_2 = \frac{1000}{50} = 20$Hz

E dividimos as frequências analizadas para checar multiplicidade:

- $df_2 = \frac{300}{20} = 15$ (A frequência analizada é um multiplo da discretização da frequência)

- $df_2 = \frac{1230}{20} = 61,5$ (A frequência analizada não é um multiplo da discretização da frequência)

Assim vemos que haverá erro de vazamento somente na frequência de $1230$Hz, uma vez que ela não é múltipla da frequência de amostragem.

##### d) Caso o tempo total de amostragem máximo admitido em função do sistema for de 500ms, qual seria o número total de amostras coletadas para atender esse o tempo de coleta sem obtenção de erros de vazamento? (5 pontos).

Para não haver erros de vazamento, precisamos de um valor de $df$ que seja múltiplo comum de $300$Hz e $1230$Hz. Assim, temos as seguintes opções: $[2, 3, 5, 6, 10, 15]$.

Assim, sabendo que o tempo total de amostragem é o produto do período de amostragem pelo número de pontos, podemos dizer que:

$N * T \leq 0,5s \rightarrow \frac{N}{f} \leq 0,5s$   (I)

Assim, utilizando a definição da discretização da frequência, $df = \frac{f}{N}$, podemos fazer a seguinte expressão:

$
\frac{N}{f} \leq 0,5 \rightarrow 2 \leq \frac{f}{N}
$

Que nos diz que a discretização da frequência precisa ser maior ou igual a $2$Hz. Notamos também que ao se aumentar o valor dessa discretização podemos diminuir o número de pontos aquisitados, o que é bom. Assim, assumindo-se uma frequência de amostragem de $10000$Hz, utiliza-se a discretização de frequência de $10$Hz, aquisitando-se assim 1000 pontos durante $0,1$s já nos garante os dados que precisamos para analizar os dois sinais.




