# Algumas notas sobre o laboratório da semana
Aqui estão algumas anotações e observações sobre a aula prática ocorrida em 29 de março.

O objetivo é analisar o espectro de frequência de ondas senoidais.
Existe uma parte teórica sobre o experimento.

Uma coisa é o domínio do tempo e outra é o domínio da frequência.

- A frequência de amostragem deve ser no mínimo 2 vezes maior que a frequência do sinal analisado.

- Temos a questão da frequência fantasma e também temos alguns exemplos de análise no roteiro.

- Erro de vazamento é quando a frequência de amostragem não é um múltiplo da frequência analisada. 

Usando o software NI USB-6008, podemos reconhecer a placa de aquisição de dados. Deve-se escolher a porta certa (onde a placa está ancorada).

O processamento dos dados é necessário pra análise. Temos eles já 

Precisamos criar um vetor de frequência a partir  da transformada de Fourier, precisamos de média e intervalo de confiança.

Coletamos dados de ondas senoidais de 2 KHz e 8 KHz. Variando o número de pontos.

Podemos ver da tabela, que:

- A primeira não tem erro algum
- A segunda terá erro de vazamento
- a terceira terá frequência fantasma em 2Khz.

A entrada da placa de filtro vem do gerador de sinais e a saída vai pra placa da national que é o inquisitor de sinais.

Só podemos analisar o espectro de frequência até metade da frequência de amostragem.

A placa da national é capaz de amostragens muito altas.

Faremos análise de espectro das ondas senoidais e quadráticas. O espectro de frequência com o filtro terá uma amplitude maior que os caso sem o filtro.

Nas ondas quadradas vai aparecer as frequências múltiplos.

Sabendo que a placa tem 12 bits calcule o erro de quantização 1 sobre 2 elevado a 12?

Temos 10 arquivos, com filtro, sem filtro e com número de pontos coletados no final. E qual a frequência de trabalho.



