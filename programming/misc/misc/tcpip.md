# Introdução:
Interessante mostrar as terminologias mais utilizadas: Existem vários modelos que representam a arquitetura TCP/IP, é possível se ter a rede móvel, rede doméstica, rede institucional, rede ISP regional. Elas são camadas de comunicação e estão interligadas resultando em um grupo interconectado de troca de informações, que é a internet. Apesar da diversidade, todas seguem os padrões ditados pelo protocolo TCP/IP que estudaremos na disciplina. 
Vamos estudar a borda e o núcleo da rede, e quais os protocolos são utilizados? Aliás, o que são protocolos?
Vamos ver a borda da rede, com  hospedeiros, rede de acesso, meio físico.
Vamos ver o núcleo da rede, com pacote/comutação de circuitos, estrutura da internet.
Vamos ver sobre desempenho, o que causa perda de pacotes, atraso e vazão.
Vamos ver sobre segurança.
Como funciona as camadas de protocolos e serviços.
E veremos sobre a história da internet.
"
## A internet é uma rede de computadores interconectados. Nesse contexto temos:
- Hospedeiros: São os equipamentos que são os sistemas finais, os fins desse ramo que são os receptores e lançadores finais e primários das informações. São os dispositivos que estão rodando os aplicativos web que usam da infraestrutura de rede. Hoje em dia, com a internet das coisas, estes dispositivos vem se multiplicando exponencialmente, com todo tipo de comunicação e aplicação imaginável.
- Enlaces: São equipamentos que estão conectados, via cabo de fibra, ou cobre, ou mesmo um meio não guiado como torres de rádio e satélite. Para cada tipo de enlace existe uma largura de banda dedicada que dita o tanto de informação que pode percorrer pelo enlace de forma simultânea.
- Roteadores: São computadores intermediários que recebem informações dos enlaces e redirecionam para que ele chegue no endereço correto. São equipamentos de rota na infraestrutura de conexão e vão dês de o roteador de sua casa, até grandes centros de redistribuição de sinal de seu contratante de internet e da rede local. Eles guiam o sinal até o servidor requisitado. Ou seja, a estrutura Enlace + Roteadores ligam dois computadores hospedeiros de acordo com suas requisições de acesso.
- Protocolos: É uma regra de controle de comunicação entre os dispositivos. Assim, as mensagens seguem regras de formatação que servem para tornar estes sinais legíveis nos dois pontos da comunicação. São exemplos: TCP, IP, HTTP, Skype, Ethernet, etc...
- Internet: É a rede das redes, ou seja, tem-se uma rede local, que está conectada a uma rede regional que está conectada à rede global. Existe uma hierarquia vaga, assim, é necessário que se esteja conectado à rede local, para que se esteja conectado à regional, e assim por diante. Ela é algo público, mas existem as Intranets, que são privadas de empresas, mas usam os mesmos protocolos.
- Padrões da internet: RFC - Request for Comment, e IETF - Internet Engineering task forces. São os responsáveis pela padronização que vemos neste curso.
- Infra estrutura de comunicação: Ela observa os serviços que são requiridos e fornece Enlaces e roteadores capazes de suportar eles. Estes serviços podem ser Web, VoIP, e-mail, jogos, e-commerce, compartilhamento de arquivos.
- Serviços de comunicação fornecidos à aplicação: Entrega de dados confiável ou não confiável. Existe uma comunicação entre as aplicações e o modal de transporte, de forma que a aplicação consegue dizer se a informação pode ser transportada com mais ou menor rigor ou confiabilidade. Isso oscila muito por exemplo entre o email e serviços de streaming como twitchTV. Existem protocolos para assegurar a informação, mas nem sempre a aplicação opta por usar ela.

## Um protocolo é uma forma de comunicação. A língua portuguesa é um protocolo de comunicação entre dois seres humanos.
Nos protocolos de redes, ao invés de dois humanos temos duas máquinas. Ela também deve falar uma língua padrão para ser entendida pela outra máquina. O protocolo define o formato, a ordem das mensagens, e as ações tomadas sobre a transmissão e recepção de mensagens. Exemplo:

- Computador1: -Solicito uma conexão TCP. (pacotes com informações que significam essa requisição).
- Computador2: -Entendi sua mensagem, posso enviar.
- Computador1: -Solicito http://www.google.com.
- Computador2: -<arquivos> (html, js, etc...)

## Borda da rede são os hospedeiros, a rede de acesso e o meio físico.
Aqui rodam as aplicação e é onde ocorre a interação máquina homem. Aqui é onde o desktop trabalha. Podem haver dois modelos de comunicação entre hospedeiros sendo eles:
- Peer-to-Peer: Onde a estrutura é paralela e ambos os computadores são iguais na comunicação e os protocolos são simétricos. São exemplos o Skype e o BitTorrent.  
- cliente-servidor: Aqui há uma hierarquia, onde os protocolos de comunicação são assimétricos. O cliente faz a solicitação de pacotes e serviços e o servidor está o tempo todo ligado e ouvindo atento para atender aos pedidos. São exemplos serviços de email e hospedagem de websites.

Para conectar computadores à internet é necessário provedores de acesso local. Estes podem ser de redes móveis, de redes residenciais ou de redes institucionais como escolas e empresas. Exemplos são a rede 4G, acessos wifi residenciais ou institucionais. A largura de banda (bits por segundo) varia muito entre cada modalidade. Além disso a rede pode ser dedicada ou compartilhada. O mais comum é ser compartilhada, ou seja, você usa a mesma infraestrutura de comunicação que muitas outras pessoas.

São exemplos de acesso:

- DSL: Digital Subscriber Line: É usada na infraestrutura telefônica existente. Em que passa pela central DSLAM para separar o que é telefone do que é internet, possui largura de banda de até 1Mbps de upload e 8Mbps de download. Mas sendo bem menos atualmente. A linha física é dedicada até a central telefônica.
- Hoje em dia é utilizado mais tecnologia a cabo que usa a tecnologia de tv a cabo para distribuir informação. Essa tecnologia é compartilhada, assim, as pessoas acessa o mesmo fio elétrico mas por diferença de frequência de comunicação cada um acessa uma parte da banda. Há também o sistema híbrido, onde a internet é a cabo até um sistema de distribuição a partir da qual passa a ser óptica, além de, é claro, a em fibra óptica completa, que vai até o seu roteador via fibra óptica. 

Todas essas tecnologias chegam até o modem em sua casa, que possui o endereço IP real. Esse modem se conecta a um roteador, que distribui a conexão entre os dispositivos de final de curso dentro de sua casa via protocolo NAT, além disso normalmente ele possui Firewall. Esse roteador local também pode distribuir as informações via wifi ou cabo Ethernet.

Outra forma é nas redes institucionais que podem ter Ethernet switches e roteadores ao lado de servidores e roteadores em toda uma infraestrutura interna de rede, mas claro, também ligada à internet externa via um roteador institucional que também pode ter firewalls e outras estruturas de segurança. Essa conexão com o mundo externo é feita a partir de um ISP (institutional link to internet).

Acessos sem fio podem ser pontos de acesso de wireless LAN, que podem ser 802.11b/g/n, que são as WI-FI que existem nas casas e tem taxas de transmissão menores que a cabo e são projetadas para pequenas distribuições. Além delas você pode ter as de wide-area, que são fornecidas através de grandes antes, com serviços de empresas de telecom como 3G e 4G.

Quando queremos enviar uma mensagem pela internet, pegamos nossa informação e dividimos em pacotes de tamanho L, e transmitimos esses pacotes a uma taxa R, assim, a velocidade de transmissão da informação depende diretamente da largura de banda e dessa taxa de transmissão de pacotes. (bits por segundo)

Esses bits caminham pelo meio físico, onde os bits são propagados pelos pares emissor receptor através dos enlaces físicos que ficam entre eles. Esses enlaces podem ser via meio guiado (o sinal se propaga por meio sólido como cobre ou fibra), ou fia meio não guiado, que é pelo ar, via rádio. Um dos meios de se fazer essa conexão física é a partir dos cabos trançados. (TP) Estes são os famosos cabos azuis com vários fiozinhos. Eles podem ter de 3(telefones tradicionais) a 5(Ethernet) fios. Também há o cabo coaxial e o de fibra ótica. Esse último tem baixíssima taxa de erro por não sofrer de interferência eletromagnética. Na situação do rádio a informação é transmitida de forma eletromagnética onde não há fios no enlace. Há efeitos do ambiente de reflexão, obstrução e interferência. Há os modais de micro ondas, LAN, e 3G. Além destes há o canal via satélite em que há um certo delay devido às altas distâncias que o sinal deve percorrer até a orbita do satélite.

## O núcleo da rede consiste na infraestrutura de distribuição da informação.
Ele consiste de uma malha de roteadores. Assim um componente da borda envia uma informação, que é dividida em pacotes e esses pacotes são enviados pela rede. Em dado momento pode ocorrer a comutação de circuitos onde mais de um pacote é passado pelo mesmo caminho ao mesmo tempo. Para isso ocorre as divisões em FDM e TDM que são respectivamente por divisão de tempo ou divisão de frequência. Ou seja, pode haver um revesamento da banda para os pacotes no tempo, ou a transmissão deles ao mesmo tempo, mas em diferentes frequências. Assim, se houver vários slots para conexão, mas nem todas forem utilizadas, a velocidade é diminuída. Isso se chama multiplexação de frequências ou por divisão do tempo. A comutação de pacotes é a separação de um informação em pacotes e esses são enviados por vários caminhos. É possível que alguns pacotes cheguem e outros não. Uma das formas em que se podem perder pactes é por enfileiramento, em que um enlace antes de um roteador é muito mais rápido que o posterior o que causa um acúmulo de dados neste nó. Se esse acúmulo ultrapassar a memória da máquina, ela começa a perder pacotes. Em cada roteador eu tenho uma tabela de roteamento, que diz para qual caminho se deve enviar um pacote baseado no endereço que consta em seu cabeçalho. A permutação de pacotes permite que mais pessoas possam usar a rede de computadores.
- Comutação de pacotes permite a mais pessoas o acesso à rede uma vez que existe uma probabilidade delas estarem usando o enlace compartilhado ao mesmo tempo, e, normalmente, essa probabilidade é bem baixa. Assim, se um enlace tem 10 slots, mesmo assim, se 35 usuários usarem a rede simultaneamente, ainda assim, a probabilidade de mais de 10 estarem ativos ao mesmo tempo é menor que 0,004. A comutação de pacotes é ótima para dados em rajadas. É muito simples e tem recursos compartilhados. O problema é que pode ter congestionamento excessivo que resulta em atrasos e perda de dados.

Exemplo humano: Em um prédio muito grande, 

A estrutura da internet, que é a rede das redes, são ligadas entre si (ISP's) de muitas formas. Uma delas é um monte ligados entre si, ou pode haver uma aproximação hierárquica. A interconexão direta entre todos os IPS não é escalonável, pois necessita de O(N^2) enlaces. Sendo de aproximação hierárquica, várias redes locais se conectam com uma rede regional e alguns também conectam-se entre si. As redes regionais também por sua vez todas se conectam com a rede nacional e entre si. (podem haver muitas redes nacionais também). E as redes nacionais conectam-se entre si via cabos submarinos. Essa rede de hosts e clientes é a estrutura da internet.

## Desempenho da rede:
Como os pacotes vão se enfileirar quando o enlace de saída é mais lento que o de entrada, dados são perdidos ou atrasados. O atraso da passagem de informação no nó pode ser definida como : D_nodal = D_processamento + D_fila + D_transmissão + D_propagação.
- D_processamento: verifica erros de bits que possam ter ocorrido no enlace de chegada, determina enlace de saída. Isso ocorre normalmente em micro-segundos.
- D_fila: Tempo de espera para transmissão no enlace de saída. Isso depende do nível de enfileiramento (congestionamento) do roteador.
- D_transmissão: Temos R=largura de banda do enlace (bps), L= tamanho do pacote(bits) e o tempo para enviar=L/R.
- D_propagação: d= tamanho do enlace, s= vel. de propagação (~2x10^8 m/sec), atraso de propagação = d/s.

Uma analogia com o mundo real é  da caravana de carros. Estes carros se propagam a 100 km/h, as cabines de pedágio levam 12 s para atender um carro(tempo de transmissão), temos que cada carro é um bit e cada caravana é um pacote. Assim, esses carros podem se acumular em alguma cabine, dependendo da velocidade de atendimento. Existe uma equação para medir isso: R= largura de banda(bps), L= tamanho do pacote(bits), a= taxa média de chegada de pacotes. Assim, a intensidade de tráfego pode ser medida com L*a/R. Se essa relação for próxima a zera, não há bloqueio e o atraso por enfileiramento é pequeno. Se for menor que 1, atrasos tornam=se brandes a medida que deixam o zero. Se for igual a 1 o atraso médio torna-se infinito e pacotes deixam de ser entregues no destino.

Para resolver essa questão, tem-se o programa Traceroute que fornece medida do atraso da origem ao roteador ao longo do caminho de fim a fim da internet para o destino. Para todo i: - envia três pacotes que alcançarão roteador i no caminho para o destino. - roteador i retornará pacotes ao emissor. Emissor temporiza intervalo entre transmissão e resposta. Quando um nó perde pacote ele pode requisitar a retransmissão do nó anterior. 

Vazão é a medida de bits/unidade de tempo de transmissão de dados no enlace. E essa medida média de todo o percurso dos dados é igual ao do enlace de menor performance. Esses enlaces são chamados de "enlace gargalo" pois eles que atrasam todo o processo.


## Camadas de protocolo e modelos de serviços:
Redes são complexas, pois temos muitas partes: Hospedeiros, roteadores, enlaces de vários meios físicos, aplicações, protocolos, hardware, software. Assim, organizamos tudo isso em uma estrutura em camadas. Cada camada oferece servições e ações para a camada superior. A modularização facilita a manutenção e a atualização do sistema.

Assim, as camadas que temos são:

- Camada de Aplicação: temos o suporte a aplicação de rede, com FTP, SMTP e HTTP.
- Camada de transporte: temos a transferência de dados processo processo com TCP e UDP.
- Camada de rede: temos o roteamento de datagramas da origem ao destino com IP e protocolos de roteamento.
- Camada de enlace: Temos a transferência de dados entre elementos vizinhos da rede, como PPP e Ethernet.
- Camada física: São os bits nos fios, ou no ar.

No modelo de referência ISO/OSI temos:
- Camada de apresentação: permite que a aplicação interprete significado de dados com criptografia, compactação e conveções específicas da máquina.
- Camada de sessão: Trata da sincronização, verificação e recuperação de dados. Ambas essas camadas não existem no protocolo TCP/IP, pois ambas estão dentro da camada de aplicação. Algumas aplicações necessitam ou não desses serviços e de diferentes rigores, assim é dada a liberdade ao programador de implementa-los conforme a necessidade e da forma que for necessária. 

Entre essas camadas ocorrem encapsulamentos da informação. No hospedeiro ocorrem os seguintes encapsulamentos:

MENSAGEM (gerada na camada da aplicação)|M|  >>  segmento (gerado na camada de transporte) |Ht|M|  >>  datagrama (gerado na camada de rede) |Hn|Ht|M|  >> quadro (gerado na camada de enlace) |HI|Hn|Ht|M| >> (na camada física tudo isso é passado em formato de bits sem adição de informações).

Quando a mensagem chega em um comutador ele desencapsula os dados somente para checar o endereço de envio, e então encaminha para o próximo elemento da rede. Quando esses dados chegam em um roteador, mais uma vez, ele desencapsula os dados e analisa até a camada de rede. Encapsula novamente e envia para o próximo elemento da rede. Chegando no destino os dados são desencapsulados até a camada de aplicação. 

É possível usar o wireshark para analisar esses pacotes até mesmo as camadas. Podemos ver da camada da aplicação até a camada física. Ele só cria cópias dos pacotes que estão entrando e saindo do computador e disponibiliza para análise.

## Wireshark 
Ele mostra o tempo, a fonte e o destino de cada pacote. Também mostra o protocolo (tcp, http), o tamanho e a informação que está sendo mandada ou recebida.
Ele mostra a camada física, de enlace, de internet, de transporte e de aplicação (nessa ordem, na janela do maio, quando disponível). Todas as características nessas camadas serão exploradas no curso. 

## Segurança 
Precisamos defender as redes contra ataques. Assim é necessário se projetar arquiteturas resistentes a ataques. A internet foi criada a um primeiro momento sem preocupações de segurança. Ela foi pensada somente como uma forma de comunicação remota entre clientes confiáveis. No entanto, pessoas más podem colocar Malware (programas maliciosos) nos hospedeiros. Eles podem entrar através de um vírus, worm ou cavalo de Troia. O malware do tipo spyware pode registrar toques, teclas sites visitados na web e enviar as informações coletadas para um servidor. O hospedeiro infectado pode também ser alistado em uma botnet, que pode ser usada para spam e ataques DoS (de negação de serviço).
O Malware normalmente é auto-replicável assim o hospedeiro infectado pode por sua vez passar o programa malicioso adiante.
Temos:
- Cavalo de Troia: Ele se aloja de forma oculta dentro de um software útil. Hoje em dia ele pode vir em uma página web(Active-X, plug-ins);
- Vírus: Infecção ao receber objetos, como anexado a emails. Ele é auto-replicável e necessita ser executado ativamente.
- Worm: Infecção recebendo passivamente objeto a ser executado. Também é auto-replicável.

O ataque Dos (Denial of service) consiste na mobilização de um grande número de computadores ou agentes de borda da rede, e estes enviam pacotes para um servidor alvo que não é capaz de lidar com o tráfego exagerado de informações.
Temos o farejamento de pacotes, em que há o meio broadcast (Ethernet compartilhada, sem fio) e um computador malicioso examina os pacotes que navegam por essa rede. (usando o wireshark, por exemplo). Assim, o meliante é capaz de ver senhas e outras informações.
Temos também o IP spoofing, em que enviamos pacotes com endereço de origem falso. Assim é possível se modificar a carga útil para atividades espúrias.

## História
- 1961: Iniciou-se a comutação de pacotes.
- 1967: Surgiu a arpanet, que foi concedida pela arpa, para instituições de pesquisa.
- 1969: Primeiro nó operacional.
- 1972: Demonstração pública da arpa com 15 nós. Primeiro protocolo (NCP) Escrita de aplicação para ambientes em rede. Primeiro programa de email.
- 1976: Ethernet na xerox parc.
- 1979: ARPAnet tem 200 nós. Nesse momento se pensou na neutralidade da rede.
- 1983: Implantação do protocolo TCP/IP. DNS definido para tradução entre nome-endereço ip 
- 1985: Protocolo ftp.
- 1988: Controle de congestionamento tcp. 100000 de usuários.
- 1990: a ARPAnet é aposentada.
- 1990: início da Web, hipertexto, html, http.
- 2007: 500 milhões de hospedeiros. voz e vídeo por ip. Aplicações p2p.

## Camada de enlace
Hospedeiros e roteadores somos nós. Canais de comunicação que conectam a nós adjacentes pelo caminho de comunicação são **enlaces**. Existem enlaces com fio (cabos submarinos ou elétricos) e enlaces sem fio(Antenas de distribuição) e reses LAN(wifi).

     <computador>----ethernet-----|roteador|------------------|roteador|---------------<acesspoint>

                       (quadro 1)                  (quadro 2)                 (quadro 3)

Em cada quadro há serviços, como por exemplo detecção e correção de erros. Em cada um desses a informação(datagrama) é codificada de forma diferente (quadro diferente). Assim o data grama é formatado de acordo com o protocolo do modal de transmissão. 

Dentro da camada de enlace, o enquadramento é o serviço que me dá acesso à camada de enlace, o data grama é encapsulado e é adicionado um cabeçalho, com endereço, dentro da camada de enlace. Isso é diferente do IP. O IP é o endereço lógico, enquanto o MAC é o endereço físico. Além disso, pode haver serviços de checagem de erro ponto a ponto. O endereço MAC assim está disponível no cabeçalho do quadro e muda conforme muda o enlace. A placa de internet é responsável por desenvolver o primeiro cabeçalho e endereço MAC ao enviar informações do computador. A partir dali essas informações são mudadas pelo roteador e assim por diante.

Dentro da camada de enlace pode haver um controle de fluxo. Se algo está sobrecarregado, pode haver um controle de fluxo no enlace, onde os dois pontos se comunicam para diminuir o tráfego. Se a comunicação for full duplex, os dois pontos podem mandar informações um para o outro simultaneamente.

A placa de rede do computador tem a responsabilidade de ser o primeiro enlace. Ela tem hardware, software e firmware que garantem seu funcionamento. Ele gera o primeiro quadro que encapsula o datagrama junto com dados de verificação de erro, entrega confiável, controle de fluxo, etc...  O adaptador receptor recebe esse pacote e usa os dados acoplados à informação para checar se há erro.

## Detecção de erros
Aqui temos o código responsável pela detecção e correção de erro. Temos o EDC que são bits de redundância responsáveis por isso. O método não é 100% confiável. Quanto maior o EDC melhor e mais confiável é o processo. Esses bits EDC são redundâncias de informação. Há diversas técnicas para detecção e correção de erro: 

- Paridade de único bit: Detecta erros de único bit. Ele soma todos os nos dados e grava o resultado no EDC (se houver um número par de um's, o EDC é 0 e se for impar é 1). O problema desse método é que se houver dois bits invertidos isso pode gerar um falso negativo na análise de erro.
- Paridade bidimensional: Cria uma matriz de bits com os dados e checa a soma dos bits coluna a coluna e linha a linha, gerando dois vetores de bits resultantes, que por suas vez também são somados.
- Soma de verificação da internet: Também conhecido como checksum. Ao transmitir uma lista de números o remetente envia também a soma negativa destes números. Assim, no destino, o receptor soma todos os números e soma com o valor de checagem esperando um resultado nulo.
- Existe também o método de verificação por redundância cíclica (crc): Ele cria bits adicionais de forma a criar uma redundância no sinal. Esse método de checagem é muito seguro e usado em modais pouco confiáveis como LANs.


## Protocolos de acesso múltiplo 
Existem dois tipos de "enlace", o ponto a ponto, que pode ser o PPP de acesso discado, ou o cabo Ethernet que conecta o comutador e o hospedeiro. E também há o broadcast, de fio ou meio compartilhado. O Ethernet a moda antiga,ou HFC e o LAN sem fio 802.11.
Para o caso do broadcast devem haver métodos de gerenciar esse acesso múltiplo para que não hajam colisões e os dados se misturem. Pra isso existem os protocolos de acesso múltiplo. Assim, esses algoritmos determinam quando um nó pode transmitir. A comunicação responsável por coordenar isso deve ser feita pelo próprio enlace. Ou seja, nada de canais paralelos ponto a ponto para coordenar o enlace broadcast.
Um canal de broadcast de velocidade R bps:
- quando um nó quer transmitir, ele pode enviar na velocidade R.
- quando M nós querem transmitir, cada um pode enviar na velocidade média de transmissão M/R.
- é totalmente descentralizado, isso é, nenhum nó é especial para coordenar a transmissão e não há sincronia de clocks entre os agentes.
- é simples.

Há três classes de protocolo MAC:
- Particionado em canais: divide o canal em "pedaços"(intervalos de tempo, frequência ou código), aloca pedaços ao nó para uso exclusivo.(FDMA e TDMA)
	- TDMA: time division multiple access. Neste o acesso ao canal é dividido em rodadas. Cada estação recebe intervalo de tamanho fixo a cada rodada. Os intervalos não usados ficam ociosos. Um exemplo é a LAN.
	- FDMA: Frequency division multiple access. Espectro do canal é dividido em bandas de frequência. Cada estação recebe banda de frequência fixa. Tempo de transmissão não usados nas bandas de frequência ficam ociosos.

- Acesso aleatório: canal não dividido, permite colisões e ele se "recupera" de colisões.(ALOHA, CSMA, CSMA/CD, CSMA/CA). Todos os pacotes enviados podem usufruir da velocidade total de banda. Não há coordenação a priori, mesmo que haja mais de um nó transmitindo ao mesmo tempo. Ocorrem colisões. O protocolo MAC de acesso aleatório especifica como detectar colisões e recuperar o sinal. São exemplos de protocolo MAC de acesso aleatório os slotted ALOHA, ALOHA, CSMA, CSMA/CD, CSMA/CA:
	- Slotted ALOHA: todos os quadros são do mesmo tamanho, o tempo é dividido em intervalos discretizados, o suficiente para transmitir um quadro. Os nós começas a transmitir somente no início destes intervalos discretizados de tempo. Assim os nós são sincronizados.Se dois ou mais nós transmitem no mesmo intervalo, todos os nós detectam a colisão. Detectada a colisão o nó tentará novamente na próxima rodada, mas um passo a frente. E isso se repete até conseguir. O lado ruim é que os emissores devem estar sincronizados e ocorrem muitas colisões. Na melhor das hipóteses o canal é utilizado para transmissões úteis em somente 37% do tempo. A probabilidade de sucesso pode ser calculada com Np(1-p)^(N-1).
	- ALOHA puro: O tempo não é discretizado, ou seja, os canais não precisam estar sincronizados. A probabilidade de colisão aumenta. Pois uma informação pode começar a ser transmitida no meio da transmissão de outra.
	- CSMA: Acesso múltiplo com sensoriamento da portadora. Ela consiste no princípio de se ouvir antes de falar. Ao se observar um canal ocioso, transmite o quadro inteiro. Se percebe canal ocupado adia transmissão. Mas mesmo assim dois canais podem acabar transmitindo ao mesmo tempo (dentro de uma janela de temo que não permita que eles se percebam). Nessa situação o tempo de transmissão do quadro inteiro é desperdiçado.
	- CSMA/CD: O mesmo do anterior, mas com detecção de colisão. Quando se nota uma colisão os canais param evitando o desperdício de tempo. A detecção é facilmente implementada em LANS com fio, pois basta se medir a intensidade do sinal. Mas é complicado em redes sem fio.

- Revezado: os nós se revezam, mas os nós com mais a enviar podem receber mais tempo.(Reservation, Polling, Token passing). Neste os nós se revezam. Se por um lado o particionado é bom para alta carga, com muitos nós, mas ineficaz para baixa carga, enquanto o de acesso aleatório é bom para baixa carga, ou seja, o contrário, o acesso revezado procura o melhor dos dois mundos.
	- Polling (seleção): nó mestre convida nós escravos a alterarem a transmissão. Normalmente usado com dispositivos burros. Mas isso pode abrir margem para sobrecarga no processo de seleção, latência e no fato de haver somente o ponto de falha do mestre.
	- Permissão: a permissão de controle é passada de um nó para o outro sequencialmente.

## Sobre o endereçamento ARP(address resolution protocol):
Endereço IP (internet protocol) é o endereço para a interface usado na camada de rede (internet). Enquanto o endereço MAC (Media Access Control)(ou LAN ou físico ou Ethernet) tem a função de levar um quadro de informação entre dois pontos de uma interface conectada fisicamente. O endereço MAC tem 48 bits para a maioria das LANs. Na ROM da NIC, às vezes também configurável por software. Exemplo: 1A-2F-BB-76-09-AD. Todo adaptador LAN tem um endereço exclusivo como o exemplificado. A alocação dessas identidades é feita pelo IEEE (institute of electrical engineers). Fabricantes compram parte do espaço de endereços MAC (para garantir exclusividade). Assim ele é imutável e único da sua máquina. O IP é diferente. Ele é atribuído com base da sub-rede ip a qual o nó está conectado. Uma analogia boa é que o MAC é a identidade enquanto o IP é o CEP. Cada nó IP possui uma tabela ARP que mapeia os endereços MAC em endereços IP. Ele pode mudar, o TTL (time to live) é o tempo após o qual o mapeamento de endereço será esquecido (normalmente 20 min). Assim essas tabelas são continuamente renovadas a todo momento. Quando o seu computador quer enviar dados para outro, ele envia o datagrama com o endereço ip de destino e MAC do roteador mais próximo, e esse mac vai sendo atualizado até chegar no IP requisitado.


## Ethernet (IEEE 802.3)
Tecnologia LAN com fio "dominante". Ela é barata e foi a primeira tecnologia LAN utilizada em larga escala. Ela é mais simples e barata que LANs de permissão e ATM. Ela foi capaz de acompanhar a corrida de velocidade 10mb/s até 10Gb/s. Antigamente também era usado para redes intra computadores, em que todos compartilhavam o mesmo barramento e colisões podiam ocorrer. Hoje em dia é organizado em formação em estrela, com um comutador central que organiza as mensagens. O quadro de Ethernet simplesmente acopla 8 byts à informação. 7 são com o padrão 10101010 e o último com o padrão 10101011. Isso é usado para sincronizar o clock do remetente e receptor. Endereços: 6bytes, se adaptador recebe quadro com endereço de destino combinado, ou com endereço de broadcast (p.e., pacote ARP), passa dados do quadro ao protocolo de camada de rede caso contrário, adaptador descarta o quadro. Então vem o tipo que indica o protocolo de camada mais alta (internet), ip, por exemplo. E, depois da carga útil, (46 - 1500 bytes) vem o CRC, que é o verificador de erros(4bytes).





## Características de redes não guiadas:
Redes de computadores com meio não guiado, ou seja, laptops. palmtops, pdas, telefones. Prometem acesso livre à internet a qualquer hora. Há dois desafios importantes:
- Sem fio: Comunicação por elance sem fio
- Mobilidade: Tratar de usuários móveis que mudam de pontos de acesso. 

O hospedeiro de uma rede sem fio é um equipamento para meio não guiado. Ele não tem fio. Eles são capazes de executar aplicações. Eles podem ser estáticos ou não estáticos, como um computador conectado via wi-fi, ou um laptop ou celular. Assim, sem fio nem sempre caracteriza mobilidade, uma vez que a rede WI-FI, por exemplo, limita o alcance do ponto de acesso.
Sempre tem uma estação base, que possui um relay, que liga o modal sem fio a uma rede guiada. Como torres de celulares, pontos de acesso 802.11. Temos também os enlaces sem fio, que permitem a comunicação entre os dispositivos móveis às estações base. Um protocolo de acesso múltiplo permite a conexão simultânea de vários hospedeiros. Existem padrões de largura de banda por método de conexão. Existem limites de abrangência (alcance) e banda para cada modal. Pode ser também uma red ad hoc, que não possui base. Seria uma conexão peer-peer, mas eles comunicam entre si informação.

- No modo infraestrutura a comunicação é centralizada, ou seja, todos os hospedeiros se comunicam com a mesma entidade.



## Camada de rede:
Na camada de rede nós temos o endereço lógico. Temos sub-serviços também, como:
Endereço lógico é diferente de endereço físico. O endereço físico é o MAC, enquanto o endereço lógico é o IP.
- modelos de serviço da camada de rede;
- repasse versus roteamento;
- como funciona um reteador;
- roteamento (seleção de caminho);
- lidando com escala;
- tópicos avançados: IPV6;

Instanciação, implementação na internet. Ao invés de falarmos de quadro, falamos de datagrama.


## Funções da camada de rede
Uma das funções da camada de rede é o roteamento. Nesse processo, o reteador em questão desencapsula a camada de rede e observa o endereçamento de origem e destino. O roteamento ocorre com a determinação do caminho de repasse dessa informação. Isso ocorre a partir de tabelas de roteamento. Existem algoritmos de roteamento para fazer essa determinação. 
O repasse é passar por um cruzamento, e você ir para a via certa. O roteamento é o estabelecimento da rota. Sabendo-se as ruas pelas quais você ira passar. O roteador cria tabelas de roteamento com base em algoritmos de roteamento. Essa tabela diz, com base no endereço de destino, pra onde encaminhar a informação, isso ocorre em todo roteador. Também é possível a criação de caminhos virtuais, uma conexão virtual. 
Existem serviços, na camada de rede, para determinadas necessidades de broadcast.

 Arquitetura  | modelo        |   Garantia de    | Garantia     |  Ordenação | Temporização | Indicação de 
     rede     | de serviço    | largura de banda | contra perda |            |              | congestionamento
 .............................................................................................................
 Internet     | Menor esforço |    Nenhuma       |  Nenhuma     |  qualquer  | Não mantida  | Nenhuma
 ATM          |     CBR       | Taxa constante   |   sim        |  Na ordem  | Mantida      | previne
 ATM          |     CBR       | Mínima garantida |   sim        |  Na ordem  | Não mantida  | previne

Dessa forma se observa que o protocolo ATM tem features ajustáveis. Existe um preço agregado dependendo das necessidades que existem dentro de uma camada de rede.
Esses serviços são análogos aos que se encontram dentro da camada de transporte (no computador), mas eles ocorrem no núcleo, ou seja, entre roteadores, estabelecendo circuitos virtuais. 
O comportamento do circuito virtual é parecido com um circuito telefônico. Deve existir uma chamada pra o estabelecimento do circuito virtual. Os pacotes não carregam o endereçamento, mas sim um identificador interno da rede virtual. A própria rede virtual já possui esse endereçamento. Pois ela fecha especificamente a conexão entre dois computadores.  
Assim, esse circuito consiste em um caminho origem - destino. O pacote carrega o número do circuito virtual (existe um para cada camada de enlace, que seria o identificador de nó do circuito virtual, isso funciona como um conjunto de placas que direcionam os pacotes pela rede de enlaces.) Essa tabela de repasse é paralela á tabela de roteamento. Esses números são mantidos enquanto o circuito virtual for mantido.
Outras tecnologias que fazem isso são frame raly e x25. Isso não é usado na internet.


O formato padrão da internet é o de rede de datagramas. Nesse tipo não há o estabelecimento de uma chamada na camada de rede. Não há estado de conexão fim a fim. Não existe um conceito de conexão, cada pacote pode seguir seu próprio caminho pela rede. Passa-se o endereço de destino de cada pacote. 
Nas tabelas de roteamento, o roteador configura intervalos de ips nos quais ele direciona cada qual para cada saída do roteador. Para isso, ele tem "IPs incompletos", isso é, ips sem os 4 octetos completos, e ele encaminha o pacote cujo ip de destino tem mais bits em comum com o designado para a porta.

Desse forma temos as duas formas de serviço mais utilizadas, o da internet (baseado em datagramas), e o serviço de circuito virtual (CV), que é parecido com telefonia, mas capaz de transmitir todo tipo de pacote.
O primeiro é um serviço elástico, sem requisitos de temporização estritos, podem se adaptar a mudanças na rede de transmissão a qualquer momento. A complexidade é muito baixa no núcleo, ela é concentrada na borda (computador cliente e servidor), e aceita muitos tipos de enlace. Já o segundo tem requisitos de temporização estritos e confiabilidade. A complexidade encontra-se dentro da rede.


## O que há dentro de um roteador?
A principal função é executar os algoritmos de roteamento (RIP, OSPF, BGP) e repassar os datagramas para os endereços corretos. Primeiramente, ele recebe os bits da camada física (em bits), depois ele desencapsula os dados da camada de enlace, depois ele observa o endereçamento na camada de rede e envia baseado na tabela de roteamento. Se o processo de encaminhar demora mais que o de receber os dados, pode-se formar uma fila logo após o desencapsulamento da camada de enlace. 
Roteadores de primeira geração são parecidos com computadores tradicionais. O controle de comutação de pacotes e de repasse é dependente da velocidade do processador. Além disso os pacotes devem ser copiados para a memória do sistema antes do repasse. Assim há duas travessias de barramento por datagrama.
Também podem haver comutação por um barramento. O datagrama da memória da porta de entrada é passado diretamente para a memória da porta de saída. Isso é bem mais rápido, até para 32Gb/s.
Existe ainda uma outra forma de roteamento que é via comutação por uma rede de interconexões. O datagrama é dividido em células de tamanho fixo e elas são passadas através de um elemento de comutação. As velocidades qui vão até 60 Gbps.
Assim, podem ser dos tipos "Memória", "Barramento", "Crossbar". Em ordem de velocidade aumentando.
Na porta de saída temos um Buffer, que é necessário quando a velocidade de transmissão dentro do roteador é maior que a de transmissão pelo enlace de saída. Depois disso ele é empacotado na camada de enlace e física e deixa o roteador. Se a quantidade de pacotes ultrapassa a capacidade do buffer, ocorre perda de pacotes. Existe uma regra para a determinação do tamanho desse buffer RTT (round trip time, tipo 250ms), C (capacidade do enlace  10Gps). Assim, Buffer = RTT * C. Recentemente também precisa se considerar N fluxos (TCP), com uma nova equação igual a RTT * c / sqrt(N).
Assim, podem haver perdas tanto na entrada quanto na saída do roteador. Para isso, o dispositivo tem algoritmos de escalonamento de pacotes. Ele é bem simples, o primeiro a chegar é o primeiro a sair. Ele é chamado de FIFO(first in first out). Se o buffer chega ao fim ele destrói o fim da fila (exclui pacotes de vim de fila), ele pode também ser randômico, e pode excluir ser por prioridade. Pode se escolher isso na configuração do roteador. Para excluir por prioridade, deve haver uma informação para classificar pacotes. Isso é também configurável, como IPs de destino ou origem, etc. Também há o método RR(Round Robin), que ele também estabelece classes para os pacotes e manda um de cada de forma cíclica. Também há o método (wfq) que é o Round Robin generalizado. Onde cada fila é uma classe e ele circula entre essas filas de forma cíclica e diferentes estratégias de query podem ser estabelecidas para cada fila. 


## What the fuck is IP
Aqui existem as convenções de endereçamento. A determinação do formato do datagrama e as convenções de manuseio de pacotes. Tem-se um estrutura de dados que leva muitas informações de forma paralela aos dados que se envia. Assim, temos uma informação que pesa um pouquinho mais que os dados que se enviou. Outra coisa que pode ocorrer é a modificação do tamanho do datagrama, pois diferentes segmentos de enlace podem ter diferentes tamanhos máximos de pacote que se pode transferir. Assim, esse datagrama pode ser fragmentado sem problemas se for necessário no caminho. E no destino ele é reagrupado e desencapsulado. Assim, na estrutura de dados também ha o identificador dizendo que o datagrama foi fragmentado e como remontar a informação (em questão de ordem).

## Como funciona o endereçamento do ipv4
Falaremos do endereçamento da versão 4 (ipv4). Falaremos do endereçamento, sub-redes, endereçamento sem classe (CIDR- Classless inter-Domain), Falaremos de márcaras também.
Inicialmente o endereçamento era dividido em classe, (A, B, C e D).
Primeiramente o endereço era divididos em classes. Tínhamos a classe A:
7bits no primeiro octeto, e 24 bits representando os hospedeiros, como 10.X.X.X, que seria 00001010.xxxxxxxx.xxxxxxxx.xxxxxxxx, o campo de rede variava de 1 a 127, totalizando 127 redes classe A. Os campos de host variavam de 1 a 254. Endereço de rede 0 e endereço de broadcast 255. Isso totaliza 254 X 254 x 254 = 16772216 hosts. Na classe B teríamos 14 bits de rede, no host teríamos 16 bits, do tipo 172.68.x.x que seria 10101100.01000100.xxxxxxxx.xxxxxxxx. O primeiro campo de rede pode variar de 128 a 191, totalizando 16.320 redes de classe B. Os campos de host podem variar de 1 a 254, totalizando 64516. Na classe C, a rede tem 21 bits, o host tem 8 bits, do tipo 192.168.15.x, com 11000000.10101000.00001111.xxxxxxxx, o primeiro pode variar de 192 a 223, totalizando 2080800 redes classe c. 
O 127 é reservado para loopback, ou seja, testar softwares de comunicação, ele é o tal do endereço localhost 127.0.0.1.
A ideia de se usar subredes é reduzir o congestionamento, dar suporte a diferentes tecnologias e segurança.
Indereço IP é constituído de 4 octetos, na versão ipv4, e ele era dividido em classes. Houve a expansão para uma rede ipv6 quando o número de hosts cresceu muito. O sistema de máscaras é utilizada na criação de sub-redes que foram uma forma de expandir o protocolo ipv4, aproveitando assim endereços que não eram aproveitados em redes. Posso segmentar redes que são grupos menores. Foi deixado um exercício. dois octetos já são reservados para a rede, e como temos um 8, bits já foram emprestados para se estar dentro de uma subrede. Assim, a primeira coisa é descobrir a qual subrede esta rede pertence. Nesse exercício eu pesso que vocês identifiquem o endereço de cada subrede.
O endereço 127 é reservado para "loopback", ou seja, é o endereço da própria máquina. 127.0.0.1 por exemplo. Pode ser usado para teste de aplicações web no próprio computador. Ele é o famigerado "localhost".

## Sub rede.
A sub rede é uma técnica que permite dividir um bloco de endereços IP atribuídos como rede em intervalos, em vários blocos de endereços menores, para um uso mais eficiente. Assim pode-se dar suporte a tecnologias e aumentar a segurança.
Para trabalhar com sub rede normalmente trabalha-se com máscaras. Ela serve para separar as subredes. Assim podemos ter classes:

- A = 255.0.0.0    - 11111111 00000000 00000000 00000000
- B = 255.255.0.0  - 11111111 11111111 00000000 00000000
- C = 255.255.255.0- 11111111 11111111 11111111 11111111

Assim, essa máscara é usada no calculo do ip do computador de destino e no ip do computador de origem. Resultados idênticos denotam computadores na mesma rede (contato direto). Se o resultado for diferente então as redes estão em redes distintas. 
Ela é criada posicionando-se TRUEs nas posições dos bits relativos à rede. Os bits da subrede são determinado com a adição dos bits tomados por empréstimo.
exemplo:
Na classe C temos: 255.255.255.0, onde o último octeto é reservado para hosts. Não só isso, mas ele pode perder bits para descrever a sub rede. Ou seja:

255.255.255. -->  _ _ _ | _ _ _ _ _   (três bits do último octeto são usados para designar a sub rede).Nesse caso podemos criar 2^2 = 8 sub redes. (Considerando a regra que o primeiro é para endereço de rede e a última que é endereço de broadcast temos 6 endereços válidos). O número de hosts que podemos ter são 2^5 = 32 hosts.

exemplo: 
Dado o número de IP 143.107.1.45 e a máscara 255.255.0.0, com endereço de rede: 143.107.0.0 e endereço de broadcast: 143.107.255.255, quantos bits foram emprestados?
143.107.00000000.00000000 ... 255.255.00000000.00000000
143.107.00000001.00101101 ... 255.255.00000000.00000000
143.107.11111111.11111111 ... 255.255.00000000.00000000
Neste caso nem um bit foi emprestado.

Para o caso de máscara 255.255.255.192
143.107.0 0 0 0 0 0 0 1.0 0 0 0 0 0 0 0
143.107.1 1 1 1 1 1 1 1.1 1 _ _ _ _ _ _ assim vemos que 10 bits foram emprestados para endereço de rede.
143.107.0 0 0 0 0 0 0 1.0 0 1 1 1 1 1 1

Se temos uma máscara de 255.255.255.240, temos:

11111111.11111111.11111111.1111_ _ _ _ assim temos 4 emprestados para endereço de rede e 4 para endereço de host

                           0000.0000     |
                           até           |  para cada subrede temos 0000 até 1111 de hosts
                           1111.0000     | 

É importante ressaltar que a subrede 0 e a subrede 1 são as de rede e broadcast.

# Sub-rede: CIDR 
Hoje em dia não se trabalha mais com classes, mas sim o endereçamento Inter-Domain Routing - CIDR. Onde o endereço de subrede tem formato decimal com pontos de separação. A formatação é A.B.C.D/x, onde x é o número de bits na parte de rede do endereço.
Assim, não existe mais classes, só uma parte para endereçamento de redes e outra para hosts.

exemplo:
                    |-------24 para redes----||-host--|
200.23.16.0/24  --> 11001000 00010111 00010000 00000000

exercício:

Precisamos de 1000 hosts para atender a demanda dos usuários. Assim, crie as sub redes usando o endereço inicial de 172.1.8.0/16 fornecido pela companhia de telecomunicações e determine:
- Endereço de cada subrede;
- A máscara pra as subredes;
- Total de subredes utilizadas;
- Número máximo de hosts em cada subrede;
- Endereço de broadcast das subredes;
- Faixa de IPs que serão utilizados em cada sub rede.
 
Observa-se que já estamos em uma subrede:
172.1.00000 100 00000000 onde os dois últimos octetos são reservados pras sub redes e pros hosts.
assim:

00000 | 100 _ _ _ _ _ _ _ _  ---> está dentro de uma subrede onde há 3 bits emprestados para os hosts, e 5 para as subredes. Assim temos 2024 endereços de host, o que atende a requisição do cliente.
O primeiro endereço dessa subrede é:

(subrede 0)
172.1.0.0    -> 172.1.000000|00.00000000
até
172.1.3.255  -> 172.1.000000|11.11111111

Depois temos

(subrede 1)
172.1.4.0    -> 172.1.000001|00.00000000
até
172.1.7.255  -> 172.1.000001|11.11111111

(subrede 2) -----------------> Seria nessa sub rede que a gente operaria

172.1.8.0    -> 172.1.000010|00.00000000   -> endereço de rede.
até                                        -> endereços válidos : 172.1.8.1 até 172.1.11.255
172.1.11.255 -> 172.1.000011|11.11111111   -> endereço de broadcast.

.
. temos 64 sub redes cada uma com 2024 hosts. 1022 endereços válidos.
.

A mascara usada seria 255.255.252.0
.
Essa é a solução otimizada, mas seria possível também trabalhar com 3 bites emprestados para os bits de host.

# Sub rede VLSM 
Essa é a máscara de sub rede de comprimento variável. As máscaras de subrede são chamadas de prefixos. Os roteadores utilizam o prefixo de rede, ao invés dos bits do endereço de IP, para determinar o ponto de divisão entre o número de rede e o número de hosts. Como pode ocorrer ainda o desperdício de endereços IP para hosts dentro daquela sub rede surgiu o conceito de máscara de sub-rede com comprimento variável, chamada de VLSM.
Essa técnica permite que mais de uma máscara seja definida para um dado endereço IP. O campo "prefixo de rede estendido" passa a poder ter diferentes tamanhos de máscara. Consegue-se assim um uso mais eficiente do espaço de endereço atribuído à organização. Permite também a agregação de rotas o que pode reduzir significativamente a quantidade de informação de roteamento no nível de backbone. 

endereço ip:
                                                                 rede          host
130.5.0.0/22 (máscara de subrede 255.255.252.0) - 10000010.00000101.000000|00.00000000 

Assim, tamos mais subredes usando por exemplo 130.5.0.0/26, onde elementos do quarto octeto são utilizados para determinação da aubrede. Muitos roteadores podem ter tabelas de roteamento com sub redes de várias camadas na mesma porta. Assim, ele anexa o prefixo de forma dinâmica e diferentes máscaras são aplicadas dependendo do endereçamento.

atividade:

Dado um endereço IP 130.10.0.0/16, e utilizando a VLSM, determine as seguintes sub-redes. Fique atento ao número de hosts e sub-redes de cada interface.


           5 sub-redes         6 sub-redes          1 sub-rede
           2000 hosts           254 hosts           15000 hosts
           [roteador]          [roteador]           [roteador]
               |                    |                    |
               |                    |                    | 
               |                    |                    |
           [roteador]-----------[roteador]-----------[roteador]

Para isso podemos começar as divisões. O endereço "root" é:
130.10.00000000.00000000   ----    255.255.0.0

Para a de 15000 precisamos de 2^14= 16384
130.10.01|000000.00000000 (130.10.64.0) até 130.10.01|111111.11111111 (130.10.127.255)

Na próxima camada colocaremos o particionamento da outra rede

Para a de 2000  precisamos de 2^11= 2000    130.10.00000|000.00000000
130.10.10|001|000.00000000 (130.10.136.0) até 130.10.10|001|111.11111111 (130.10.143.255)

Para a de 254   precisamos de 2^8 = 256     130.10.00000000.|00000000

255.255.254.0 --> 11111111.11111111.11111110.00000000
              --> 11111111.11111111.11111111.11000000



## Camada de transporte
Já estamos pensando na programação. Pois isso ocorre dentro do pc. São os protocolos UDP e TCP. 
Temos as portas, ou seja, aqui já falamos de terminologias de sistema final. (fim de curso).
Temos um socket, que é aberto por uma aplicação e uma porta. Assim, quando estou desenvolvendo minha aplicação, devo pensar na camada de aplicação e na camada de transporte. Vamos começar a falar de programação. 
Existem dois mais importantes:
- UDP: transporte não orientado a conexão. Não é necessário se estabelecer uma conexão. A informação é enviada e não se sabe se ela chegou.
- TCP: Este é orientado a conexão, então ele recebe feedback pela informação que envia, neste protocolo.
A Camada de transporte não é acessada pelo núcleo da rede, assim, a informação é empacotada e só é desempacotada no destino final.

Recapitulando: Falamos já da camada física, enlace, rede e agora a camada de transporte.
Na física pensamos no sinal, como ele é formatado e transmitido. Na de enlace onde ocorre o endereçamento físico. Então temos a camada de rede, que estabelece o endereço lógico. E agora falaremos na camada de transporte.
A camada de transporte oferta comunicação lógica entre processos de aplicação rodando em hosts diferentes. Ou seja, na camada de rede ocorre a comunicação lógica entre os computadores envolvidos na comunicação, enquanto na camada de transporte temos a comunicação entre as aplicações. Ou seja, o endereço da aplicação é abstraído da camada de rede.
Temos duas categorias de atores:
- Remetente: Na camada de transporte, segmenta a informação em pacotes pequenos.
- Destinatário: Remonta a informação segmentada pelo remetente.

Diferença quanto aos serviços dos protocolos UDP e TCP:
- TCP: Controle de congestionamento, controle de fluxo e estabelecimento de conexão.
- UDP: extensão sem luxo do IP pelo menor esforço. Informações podem ser perdidas.

# Multiplexação:
Ela ocorre no remetente. Ela coleta dados de múltiplos sockets e insere em seus cabeçalhos uma identificação para auxiliar na montagem da informação no destinatário. No destinatário as informações recebidas são encaminhadas para os sockets corretos a partir dos cabeçalhos no momento da multiplexação. 
O hospedeiro recebe o data grama, cada um tem um segmento da camada de transporte. Cada segmento tem o número da porta de origem e da porta de destino. O hospedeiro usa o número IP e o número da porta para encaminhar o segmento para o socket apropriado. O socket UDP é identificado por tupla de dois elementos, endereço de IP de destino e número de porta de destino. O de TCP tem 4 elementos na tupla. Tem-se endereço de IP de origem e número de porta de origem, IP de destino e número de porta de destino. Assim, podem haver múltiplos sockets para a mesma aplicação para o caso do tcp.

Correio eletrônico | SMTP | TCP
Acesso a terminal remoto | Telnet| TCP
Web | HTTP | TCP
Transferência de arquivo | FTP | TCP
Servidor de arquivos remoto | NFS | Tipicamente UDP
Recepção de multimídia | Tipicamente proprietário | UDP ou TCP
Telefonia por internet | tipicamente proprietário | UDP ou TCP
Gerenciamento de rede | SNMP | Tipicamente UDP 
Protocolo de roteamento | RIP | Tipicamente UDP
Tradução de nome | DNS | Tipicamente UDP 

# UDP : User Datagram Protocol 
Serviço básico e sem luxo. Informação pode ser perdida ou ordem pode ser mudada dos fragmentos da informação. Não há estabelecimento de conexão (o feedback pode causar atraso), sem estado de conexão no remetente, destinatário. E não há controle de congestionamento.
Ele é normalmente usado para aplicações de stream, onde a integridade da informação não é crucial. Ele é usado no DNS, SNMP e no RIP. Pode haver um check sum, que faz uma verificação de bits invertidos. O destinatário pode checar a informação para detectar se a informação veio corrompida. Essa é uma das principais características do protocolo UDP.

# Estaelecimento de conexões confiáveis. 
É importante que se vejam as estratégias para assegurar a confiabilidade da transmissão de um sinal. Essas estratégias podem ser usadas em canais que se preocupam com a integridade das informações transmitidas, como o TCP.
Esses princípios são encarados como importantes tanto na camada de enlace quanto na de transporte e na de aplicação. As características do canal confiável determinarão a complexidade do protocolo de transferência confiável. O protocolo rdt (reliable data transfer) é complexo na medida do necessário.
Se o canal é confiável, não é necessário que os protocolos rdt sejam muito robustos. Mas, no caso contrário, se a confiabilidade não é assegurada, os protocolos de rdt são necessários. 
Assim, temos de forma incremental de transferência de dados que usam de máquinas de estado finito que ficam checando o estado atual, para especificar RE e DE.
- rdt1.0: nenhum erro de bit, não há perdas de pacotes.
- rdt2.0: Faz um check sum, reconhece erros, e faz um feedback dizendo que houve problema. Havendo problema, o remetente envia novamente o mesmo pacote. Não identifica as chamadas.
- rdt2.1: Ocorre a identificação da chamada, podendo assim identificar erros de envio de NAK.
- rdt2.2: Não usa NAK, mas sim ACK, e todo processo recebido é enviado estado de recebimento com identificação.
- rdt3.0: Tem tudo de antes, mais um timeout, onde o remetente espera por um tempo o ack. Se não for recebido, ele duplica já a informação. 
- Go_back_n: É feito em janelas de envio em paralelo.
- repetição_seletiva: repete a partir de falha, também trabalha em janelas em paralelo.

Go_back_end e separação seletiva usam paralelismo o que é ótimo. No Go_back_end, a partir do momento que não há o retorno do recebimento da informação, ele reenvia tudo novamente, após a confirmação do timeout. Já na repetição seletiva, existe um burrer no receptor e ele guarda as informação após o pacote perdido que chegarem. Assim o remetente não precisa reenviar tudo após o time out, mas sim somente o que foi perdido.

# TCP : Ele existe ponto a ponto, onde existe um remetente e um destinatário. 
Tem-se a confiança de que os dados chegarão de forma correta e em ordem. Pode-se trabalhar em paralelo com controle de fluxo e congestionamento. Os dados são enviados de forma full duplex, onde os dados são bidirecionais. O remetente não sobrecarrega o destinatário, há um controle de fluxo.
Existe o check sum para verificação dos dados. Informações de feedback e outros são anexados nos cabeçalhos do data grama. Akcs são usados para checagem de envio. A determinação de buffers e sequência de envio são controlados pelo programador na camada de aplicação. Pode-se programar time-outs, por exemplo, ou fazer as coisas em paralelo. Para estimar esse tempo de espera pode-se estimar o RTT, existem funções para estimar o tempo de ida e volta da informação.

EstimatedRTT = (2 - \alpha) * EstimatedTrr + \alpha * SampleRTT

Assim, o estimado procura um valor médio deste temo de envio, e pode variar com o tempo.
Para garantir a transferência confiável usa-se o rdp em sima do IP. Usa-se envio de seguimentos em paralelo. Há ACKs acumulativos, o tcp usa temporizador único de retransmissão. Retransmissão são trigadas por eventos de time out e acks duplicados.
Assim, inicia-se uma conexão a nível de aplicação, e iniciam-se as estratégias de comunicação, com medição de tempo de resposta e tudo que seja necessário. Até o fechamento da conexão deve ser comunicado e confirmado com ACK. Assim, a aplicação é fechada no servidor também. 
Existe também o controle de fluxo, ou seja, se o remetente envia muitos dados, rápido de mais, o destinatário pode avisar e pedir para diminuir o tráfego. Os buffers sobrecarregados sinalizam esse fato para o destinatário. O resultado de congestionamento pode ser a perda de pacotes e longos atrasos. Com um enfileiramento muito grande nos buffers. Este é um dos grandes problemas das redes de computadores. Então como tratar isso? 
Se houver mais dados que o limite de banda da conexão, começam a haver problemas. Roteadores não possuem buffers infinitos, mas aumentar a memória deles permite maior engarrafamento sem perda de dados. Aumentar a rapidez de processamento é uma solução real, mas esse é o tipo de manutenção que existe no núcleo da rede. Quanto mais hosts em uma rede mais difícil é manter a eficiência e, por consequência, as capacidades de uma estrutura de rede.
