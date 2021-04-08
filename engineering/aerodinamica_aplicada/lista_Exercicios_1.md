## Resolução primeira lista de exercícios

Author: Felipe J. O. Ribeiro (11711EAR012)

### 1 - primeira questão

![](./lista_Exercicios_1.png)

- Temos a equação da velocidade:
$\vec{V} = 4tx \vec{i} - 2t^2y \vec{j} + 4xz \vec{k}$

Separando as componentes:

$u =4tx$

$v = - 2t^2y$

$w = 4xz$

- Para calcular a aceleração fazemos a derivada total:
$
    \vec{A} = \frac{D \vec{V}}{D t} = \frac{\partial \vec{V}}{\partial t} + u \frac{\partial \vec{V}}{\partial x} + v \frac{\partial \vec{V}}{\partial y} + w \frac{\partial \vec{V}}{\partial z}   
$

Separando as componentes:

$A_x = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z}$


$A_y = \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z}$


$A_z = \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z}$

Onde observamos o termo da velocidade local no primeiro termo após a igualdade e os termos convectivos adiante.

$
A_x = 4x + u 4 t + v 0 + w 0 = 4 (x + ut) = 4(x + 4tx t) = 4x (1 + 4t^2)
$

$
A_y = -4ty + u 0 - 2 v t^2 + w 0 = -2t (2y + vt) = -2t (2y - 2t^3y) = -4ty(1 - t^3) 
$

$
A_z = 0 + u 4z + v 0 + w 4x = 4 (uz + wx) = 4 (4txz + 4x^2z) = 16xz(t + x)
$

O que nos dá o campo de aceleração final: 

$
\vec{A} =  4x (1 + 4t^2) \vec{i}-4ty(1 - t^3) \vec{j}+ 16xz(t + x)\vec{k}
$


### 2 - Segunda questão

![](./lista_Exercicios_1_2.png)

- Assume-se que $f(y)$ só está em função de y.

- Temos um campo de velocidade igual a $\vec{V} = 4xy^2\vec{i} + f(y)\vec{j} - zy^2\vec{k}$

Separando as componentes:

$
u = 4xy^2
$

$
v = f(y)
$

$
w = -zy^2
$

- Temos um fluido incompressível, logo temos:$\vec{\nabla} \bullet \vec{V} = \frac{\partial u }{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$ 

Assim, aplicando as componentes:

$
\frac{\partial }{\partial x}(4xy^2) + \frac{\partial f(y)}{\partial y} + \frac{\partial }{\partial z}(- zy^2) = 0
$

$
4y^2 + \frac{\partial f(y)}{\partial y} - y^2 = 0
$

$
\frac{\partial f(y)}{\partial y} = -3y^2
$

Integrando em y em ambos os lados:

$
f(y) = -y^3 + C
$

Em que $C$ é uma constante numérica.

### 3 - terceira questão

![](./lista_Exercicios_1_3.png)

Assumi-se um escoamento bidimensional, com $w = 0$.

Temos:
- $u = \frac{U_o}{L}x$
- $v = - \frac{U_o}{L}y$

Para calcular o vetor aceleração, calculamos a derivada total bidimensional

$
\vec{A} = \frac{D \vec{V}}{D t} = \frac{\partial \vec{V}}{\partial t} + u \frac{\partial \vec{V}}{\partial x} + v \frac{\partial \vec{V}}{\partial y}   
$

Separando em componentes:

$A_x = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y}$


$A_y = \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y}$

Substituindo na expressão:

$
A_x = 0 + u \frac{U_o}{L} + 0 = x \frac{U_o^2}{L^2}
$

$
A_y = 0 + 0 - v \frac{U_o}{L} = - y \frac{U_o^2}{L^2}
$

Isso nos dá um vetor aceleração igual a $\vec{A} = x \frac{U_o^2}{L^2} \vec{i} - y \frac{U_o^2}{L^2} \vec{j}$

Podemos ver que $A_x$ é puramente proporcional a x, e o mesmo vale pra $A_y$. Dessa forma, os vetores sempre apontam na direção da origem, o que descreve um campo vetorial puramente radial. 

Para:
- $L = 1,5$
- $|\vec{A}(1,1)| = 25$

A partir disto temos:

$\sqrt{A_x^2 + A_y^2} = 25$

$
\sqrt{(\frac{U_o^2}{1,5^2})^2 + ( - \frac{U_o^2}{1.5^2})^2} = 25
$

$
\sqrt{2 \frac{U_o^4}{1,5^4} } = 25
$

$
(\frac{U_o}{1,5})^4 = \frac{25^2}{2}
$

$
\frac{U_o}{1,5} = \pm \sqrt[4]{\frac{25^2}{2}}
$

$
U_o = \pm \frac{7,5}{\sqrt[4]{2}} = \pm 6,3067
$

### 4 - quarta questão 

![](./lista_Exercicios_1_4.png)

Sabemos que:
- Fluido incompressível.
- regime permanente(nada em função do tempo), laminar.
- bidimensional(w=0).
- Função corrente = $\psi = (Vr\sin\theta)(r - \frac{a^2}{r})$

Podemos seguir a definição da função corrente para obter as velocidades:

$
v_r = \frac{1}{r}\frac{\partial \psi}{\partial \theta} = \frac{1}{r} \frac{\partial}{\partial \theta}(V r^2 \sin\theta - V\sin\theta a^2) 
$

$
v_r = \frac{1}{r} (Vr^2 \cos\theta - V a^2 \cos\theta) = \frac{V \cos\theta}{r}(r^2 - a^2)
$

$
v_\theta = - \frac{\partial \psi}{\partial r} = - \frac{\partial}{\partial r}(V r^2 \sin\theta - V\sin\theta a^2) 
$

$
v_\theta = - 2 V r \sin\theta 
$

O que nos dá o campo vetorial de velocidades em coordenadas polares de:

$
\vec{V} = \frac{V \cos\theta}{r}(r^2 - a^2) \hat{u_r} - 2 V r \sin\theta \hat{u_\theta}
$

### 5 - quinta questão 

![](./lista_Exercicios_1_5.png)

Sabemos que:
- Escoamento em regime permanente (laminar).
- Escoamento incompressível.
- Regime bidimensional ($w = 0$).
- $\vec{V}= V\frac{y}{h}\vec{i}$
- $\psi(x,0) = 0$

Para achar a função corrente, podemos usar sua definição formal:

$
u = \frac{\partial \psi}{\partial y}
$

$
v = - \frac{\partial \psi}{\partial x}
$

Dessa forma, temos:

$
\frac{\partial \psi}{\partial y} = V \frac{y}{h}
$

$
\frac{\partial \psi}{\partial x} = 0
$

Isso nos permite dizer que:

I :
$
\psi(x,y) = V \frac{y^2}{2h} + f(x)
$

II :
$
\psi(x,y) = 0 + f(y)
$

Comparando as equações chegamos à conclusão de que:

$
\psi(y) = V \frac{y^2}{2h} + C
$

Em que C é uma constante. Nesse momento podemos aplicar $\psi(x,0) = 0$. Que resulta em:

$
\psi(0) =  V \frac{0^2}{2h} + C = 0 \rightarrow C = 0
$

Assim, a função corrente pode ser definida como:

$
\psi(y) = V \frac{y^2}{2h}
$

Vemos que ela só aumenta com o aumento de $y$ o que indica um fluido que corre para a direita ($x$ positivo). Outra observação interessante é que a função não varia em $x$, o que aponta que todas as linhas de corrente estão na horizontal.

Para o cálculo da função de potência, podemos partir também de sua definição formal bidimensional:

$
u = \frac{\partial \phi}{\partial x}
$

$
v = \frac{\partial \phi}{\partial y}
$

Dessa forma, aplicando o que sabemos:

$
\frac{\partial \phi}{\partial x} = V \frac{y}{h}
$

$
\frac{\partial \phi}{\partial y} = 0
$

Tal sistema de equações não tem solução, o que nos diz que não existe função potencial para esse caso.


### 6 - sexta questão 

![](./lista_Exercicios_1_6.png)

A partir da equação potencial, podemos achar as equações da velocidade fazendo derivadas parciais:

$
\frac{\partial \phi}{\partial x } = u = y + 2x
$

$
\frac{\partial \phi}{\partial y } = v = x - 2y
$

Dessa forma, podemos achar a função de corrente a partir de sua definição formal:

$
\frac{\partial \psi}{\partial y} = u = y + 2x
$

$
\frac{\partial \psi}{\partial x} = -v = 2y - x
$

Assim, integrando ambos, podemos obter:

$
\psi(x,y) = \frac{y^2}{2} + 2xy + f(x)
$

$
\psi(x,y) = 2xy - \frac{x^2}{2} + g(y)
$

Derivando ambas de forma cruzada obtemos:

$
\frac{\partial \psi}{\partial x} = 2y + f(x)^\prime = 2y - x
$

$
\frac{\partial \psi}{\partial y} = 2x + g(y)^\prime = y + 2x
$

O que resulta em:

$
f(x)^\prime = -x
$

$
g(y)^\prime = y
$

Que quando integrados nos dá:

$
f(x) = -\frac{x^2}{2} + C_1
$

$
g(y) = \frac{y^2}{2} + C_2
$

Assim, nossa função de corrente pode ser desenvolvida:


$
\psi(x,y) = \frac{y^2}{2} + 2xy -\frac{x^2}{2} + C_1
$

$
\psi(x,y) = 2xy - \frac{x^2}{2} + \frac{y^2}{2} + C_2
$

O que faz sentido, temos também $C_1 = C_2 = C$:

$
\psi(x,y) = 2xy - \frac{x^2}{2} + \frac{y^2}{2} + C
$

Para acharmos a equação de linha de corrente que passa pelo ponto $(2,1)$ basta acharmos o valor da função para esse ponto:

$
\psi(2,1) = 2*2*1 - \frac{2^2}{2} + \frac{1^2}{2} + C
$

$
\psi(2,1) = 2*2*1 - \frac{2^2}{2} + \frac{1^2}{2} + C = 4 - 2 + 0,5 = 2,5 
$

Assim, a equação dessa linha de corrente é igual a:

$
2xy - \frac{x^2}{2} + \frac{y^2}{2} = 2,5 - C
$

Creio que não haja informações o suficiente para descrever $C$.


### 7 - sétima questão 

![](./lista_Exercicios_1_7.png)

O que sabemos:
- Regime permanente implica em escoamento laminar.
- Bidimensional implica em $w = 0$.
- $u = V\cos\alpha$
- $v = V\sin\alpha$
- Sendo incompressível, a equação da continuidade é nula.

Para achar a função de corrente podemos usar da definição formal:

$
u = \frac{\partial \psi}{\partial y}
$

$
v = - \frac{\partial \psi}{\partial x}
$

Assim, temos:

$\frac{\partial \psi}{\partial y} = V\cos\alpha$

$\frac{\partial \psi}{\partial x} = - V\sin\alpha$

Integrando ambos:

$
\psi(x,y)= y V\cos\alpha + f(x)
$

$
\psi(x,y)= - x V\sin\alpha + g(y)
$

Derivando de forma cruzada:

$
\frac{\partial \psi}{\partial x} = f(x)^\prime = - V \sin\alpha 
$

$
\frac{\partial \psi}{\partial y} = g(y)^\prime = V \cos\alpha
$

E integrando:

$
f(x) = -V x \sin\alpha + C_1
$

$
g(y) = V y \cos\alpha + C_2
$

Substituindo nas funções de corrente:

$
\psi(x,y)= y V\cos\alpha -V x \sin\alpha + C_1
$

$
\psi(x,y)= - x V\sin\alpha + V y \cos\alpha + C_2
$

Vemos que a solução faz sentido, e que $C_1 = C_2 = C$. Isso nos dá uma função de corrente como segue:

$
\psi(x,y)= V(y \cos\alpha - x \sin\alpha) + C
$


### 8 - oitava questão 

![](./lista_Exercicios_1_8.png)
![](./lista_Exercicios_1_9.png)

Sabemos:
- $\psi(x,y)=0$ na parede.
- $\psi(x,y)=0$ longe da parede é um valor positivo.
- Considera-se o escoamento bidimensional ($w = 0$).
- Considera-se o fluido Newtoniano e incompressível.

Considerando o comportamento do fluido com a função corrente, como podemos ver nesse recorte do livro do White:

![](./lista_Exercicios_1_10.png)

A função corrente aumenta em uma linha perpendicular ao fluido que caminha com o sentido do fluido para a direita. Com isso, podemos fazer uma análise gráfica na imagem da questão:

![](./lista_Exercicios_1_11.png)

Podemos ver que a extremidade da bolha encosta na parede, o que torna o valor de sua função corrente igual a zero. Dessa forma, a bolha fica cercada por um contorna de valor de função corrente igual a zero. Também podemos ver com uma das setas que o valor da função corrente diminui dentro da bolha ao se aproximar do seu centro, tornando todos os valores ali dentro negativos uma vez que teriam de ser menores que zero. O centro dessa bolha passa a ser o ponto onde ocorre a mínima função corrente em todo o escoamento da imagem. A seta invertida na parte inferior da bolha também nos indica que a função corrente aumenta do centro dela em direção da parede.


### 9 - nona questão 

![](./lista_Exercicios_1_12.png)

- Temos um escoamento turbulento de comportamento estatisticamente permanente.
- O escoamento é bidimensional ($w = 0$).
- O escoamento é compressível.
- O bloco na imagem é um quadrado de tamanho 1.
- Linhas de corrente disponíveis para análise.
- Fluido é ar a temperatura ambiente ($\rho = 1,18 kg/m^2$).
- $\psi(x,y) [kg/ms]$

Podemos desenhar as linhas de velocidade ao observarmos mais uma vez o princípio das linhas de corrente a seguir:

![](./lista_Exercicios_1_10.png)

Observamos que a linha de corrente de valor igual a $1$ é a menor de todas, assim, a velocidade roda em torno de seu centro no sentido horário segundo a convenção das linhas de corrente. Isso nos permite fazer a estimativa da direção da velocidade nos dois pontos:

![](./lista_Exercicios_1_13.png)

Para estimar a velocidade do vento no Ponto $B$ assumimos um escoamento linear entre as duas linhas de corrente. Podemos estimar, grosseiramente, que a distância entre elas é de $0,05 m$. Sabemos que $\frac{\partial \psi}{\partial y} = u$, o que nos diz que a unidade de medida desta função é $m^2/s$, mas neste caso vemos que ela está dependente da massa do fluido. Para adimensionalizar ela nesse sentido podemos dividir ela pela densidade. Além disso, a diferença entre dois valores de função de corrente dividido pela distância das linhas, assumindo linearidade do sistema também deve nos dar a velocidade. Assim, temos:

$
 \frac{\Delta\psi}{\rho \delta} = \frac{(6 - 5)[kg/ms]}{1,18 [kg/m^3] * 0.05 [m]} \simeq 17 [m/s]
$


### 10 - décima questão 

![](./lista_Exercicios_1_14.png)

Para aplicar a equação de Bernoulli consideramos que o fluido é incompressível, irrotacional e que não há atritos com as paredes do túnel. 
- Sabemos que a densidade do ar nessas condições pode ser conseguido a partir da constante dos gases para o ar $0,287 [kPa*m^3/kg * K]$.
- Velocidade no túnel é de $80 [m/s]$

Assim, temos:

$
\rho = \frac{P}{R*T} = \frac{101,3}{0,287 * (20 + 273)} = 1,205 [Kg/m^3]
$

Fora do túnel, a pressão é igual à pressão ambiente e a velocidade é igual a zero, assim temos que $V_1 = 0$ e $P_1 = 101,3[KPa]$. A diferença na altura é negligenciável. Assim temos a equação final como:

$
\frac{P_1}{\rho} + \frac{0^2}{2} = \frac{P_2}{\rho} + \frac{V_2^2}{2}
$

$
P_2= P_1 - \frac{\rho V_2^2}{2} = 101300 - \frac{1,205 *  80^2}{2} = 97444,44 \simeq 97,4 [Kpa]
$


### 11 - décima primeira questão 

![](./lista_Exercicios_1_15.png)

- Podemos definir a densidade da água como $1000 Kg/m^3$
- Consideramos o fluido como incompressível.
- Área de entrada = $\pi (0,07/2)^2 = 0,00385 [m^2]$
- Área de garganta = $\pi (0,04/2)^2 = 0,00126 [m^2]$
- Também consideramos o fluido como completamente desenvolvido e desconsideramos atritos o que nos permite usar Bernoulli.

Pelo fluido ser incompressível, já podemos dizer que a vazão é constante. Isso nos permite declarar que:

$
A_1 * V_1 = A_2 * V_2
$

$
V_2 = \frac{A_1 * V_1}{A_2}
$

Como o escoamento é horizontal, podemos ignorar as diferenças de altura:

$
\frac{P_1}{\rho} + \frac{V_1^2}{2} = \frac{P_2}{\rho} + \frac{V_2^2}{2}
$

Substituindo em $V_2$:

$
\frac{P_1}{\rho} + \frac{V_1^2}{2} = \frac{P_2}{\rho} + \frac{(\frac{A_1 * V_1}{A_2})^2}{2}
$

$
 \frac{V_1^2}{2} = \frac{P_2-P_1}{\rho} + \frac{(\frac{A_1 * V_1}{A_2})^2}{2}
$

$
 V_1^2(1 - \frac{A_1^2}{A_2^2})= \frac{2(P_2-P_1)}{\rho} 
$

$
 V_1^2 = \frac{2(P_2-P_1)}{\rho(1 - \frac{A_1^2}{A_2^2})} 
$

$
 V_1 = \sqrt{\frac{2(P_2-P_1)}{\rho(1 - \frac{A_1^2}{A_2^2})}} = 8,624
$

Isso nos dá uma vasão de $8,624 * A_1 = 0,033$


### 12 - décima segunda questão 

![](./lista_Exercicios_1_16.png)

- Temos a vazão no tubo ($0,12[m^3/s]$) que por se tratar de um fluido incompressível é a mesma para todas as secções transversais do escoamento interno.
- Temos a densidade do ar igual a $\rho = 1,20 [kg/m^3]$, constante.
- Área 1 = $\pi (0,22/2)^2 = 0,038 [m^2]$
- Área 2 = $\pi (0,1/2)^2 = 0,00785 [m^2]$
- Também consideramos que não há atrito e que o escoamento está completamente desenvolvido.

Mais uma vez temos um escoamento horizontal, em que posemos definir Bernoulli da seguinte forma:

$
\frac{P_1}{\rho} + \frac{V_1^2}{2} = \frac{P_2}{\rho} + \frac{V_2^2}{2}
$

Podemos achar a diferença de pressão da seguinte forma:

$
P_1 - P_2= \frac{\rho (V_2^2 - V_1^2)}{2} 
$

É possível achar as velocidades dividindo a vazão pela área:

$
V_1 = \frac{0,12}{0,038} = 3,157
$

$
V_2 = \frac{0,12}{0,00785} = 15,279
$

$
P_1 - P_2= \frac{\rho (V_2^2 - V_1^2)}{2} = \frac{1,2 (15,2866^2 - 3,158^2)}{2} = 134,09 [N/m^2]
$

Para achar a altura, podemos usar a fórmula $\Delta P  = \rho g h$, que nos dá:

$
h= \frac{\Delta P}{\rho g} = \frac{134,09 [N/m^2]}{1000[kg/m^3] 9,8 [m/s^2]} = 1,37 [cm]
$


### 13 - décima terceira questão 

![](./lista_Exercicios_1_17.png)

- Considerando a densidade da água como $1000 [kg/m^3]$,
- Considerando um escoamento incompressível, em regime permanente e irrotacional.
- Também desconsideramos os efeitos do atrito, o que nos possibilita o uso de Bernoulli.
- Como os pontos de análise estão muito próximos, também se desconsidera o efeito da gravidade sobre o escoamento.

Dessa forma temos a seguinte equação:

$
\frac{P_1}{\rho} + \frac{V_1^2}{2} = \frac{P_2}{\rho} + \frac{V_2^2}{2}
$

Podemos comparar dois pontos próximos sendo um deles o orifício de frente para o escoamento e o outro o que pega o escoamento de lado. Assim, em um deles a velocidade é zero enquanto no outro não. Isso nos dá:

$
\frac{P_1}{\rho} + \frac{0^2}{2} = \frac{P_2}{\rho} + \frac{V_2^2}{2}
$

$
P_1 = P_2 + \frac{\rho V_2^2}{2}
$

A diferença de pressão pode ser pega a partir do tamanho da coluna da água, com a expressão:

$\Delta P = \rho g h$


$
\frac{\rho V_2^2}{2} = \rho_w g h
$

$
\frac{1,15 V_2^2}{2} = 1000 * 9,8 * 0,055
$

$
V_2= \sqrt{\frac{2 * 1000 * 9,8 * 0,055}{1,15}} = 30,617 [m/s]
$


### 14 - décima quarta questão 

![](./lista_Exercicios_1_18.png) 

Usando de Bernoulli mais uma vez: 
- desconsiderando atritos.
- considerando o fluido como Newtoniano e incompressível.
- considerando o o escoamento como completamente desenvolvido.

Temos a seguinte equação, observando que em um dos pontos a velocidade é zero, e tem-se um escoamento horizontal:

$
\frac{P_1}{\rho} + \frac{V_1^2}{2} = \frac{P_2}{\rho} + \frac{0^2}{2} 
$

$
P_2 - P_1 = \frac{\rho V_1^2}{2}
$

Essa diferença de pressão causa a diferença na altura de coluna de água. Isso pode ser calculado com a expressão:$\Delta P = \rho g h$

$
\rho g h = \frac{\rho V_1^2}{2}
$

$
g h = \frac{V_1^2}{2}
$

$
V_1 = \sqrt{2 h g} = \sqrt{2 * 0,12 * 9,8} = 1,534 [m/s]
$

