# Primeira aula experimental
Queremos que o aluno se familiarize com tratamento de dados advindos do sensor de temperatura do sensor LM35. Ele mostrou o docs com códigos e a montagem do sistema. Também mostrou o código em arduino para aquisição dos dados. No monitor serial aparece a temperatura do sistema. 

Como é no EAD, temos acesso ao código, mas não faremos o experimento prático e sim somente trabalharemos com o output do experimento. Ele deu uma breve explicação sobre médias móveis. Esse tipo de média é capaz de atenuar grandes variações de alta frequência.

Ele mostrou então como coletar os dados com o Matlab diretamente da saída serial do arduino. Nesse ponto que seria interessante adaptar o código ao python. O código também consta no docs.

Ele disse que precisamos ter alguma ferramenta pra ler o txt. A gente precisa somente pegar os dados do txt e armazenar eles em um vetor. Então precisamos calcular alguns valores estatísticos, como média, desvio padrão, skinless, kurtosis, etc... Todas essas coisas serão comentadas com a gente na aula da semana que vem. Pegamos o valor da medida menos a média adquirida pelo desvio padrão. Também calcularemos o intervalo de confiança estatística. Também há um programa para imprimir o histograma e a partir dos dados coletados precisa pegar os dados estatísticos, implementar alguns testes. Tudo isso será ensinado na aula da semana que vem.

Histograma segue o padrão de uma curva normal? Criamos um histograma com 6 classes e vemos quantas amostras a gente teria de uma função normal e quantas a gente teve na prática. Assim, a gente pega  a diferença entre referência e observado e coloca ao quadrado, e faz mais algumas coisas. Esse é o teste do ki quadrado?

Assim, a missão agora é pegar o txt do teams em modulo 1> Files > grupo 3.
Esperaremos a aula da semana que vem para aprendermos os métodos estatísticos.
