## Modelo de comunicação OSI(Open System Interconnection): Conhecimento introdutório para o estudo de redes TCP/IP:
---

É um modelo teórico usado para o estudo de redes. Ele tenta separar em partes (camadas) onde cada serviço executado na rede vira uma etapa no processamento da informação. Na parte física ele é encapsulado e desencapsulado no destino.
Tem-se camadas que são sete que vão dês da aplicação até a camada física:

- Física: É o conjunto de bits (zeros e ums) que deve ser enviado;
- Enlace: É a camada em que ocorre o enquadramento do conjunto de bits, ou seja, um empacotamento;
- Rede: É a camada onde ocorre o endereçamento; 
- Transporte: É onde a informação é transportada e possui várias técnicas computacionais dependendo do modal de transporte;
- Sessão: É um controle de tempo de comunicação de forma a se estabelecer uma instância de acesso;
- Apresentação: Momento onde é aplicada criptografia, ou outras ferramentas de processamento da informação;
- Aplicação: É o destino final, onde as informações serão usadas.

Dessa forma, essa arquitetura em camadas serve para separar os diferentes serviços os quais a comunicação ocorre de forma lógica, sequencial e inteligível.

A rede TCP/IP não possui as camadas de Sessão e Apresentação. Elas devem ser implementadas na camada de aplicação.

                                      Layer (OSI names)
+-----------------------------------+
|  TELNET    FTP     SMTP    DNS    |   applications
|-----------------------------------|
|        TCP            UDP         |   Transport
|-----------------------------------|
|               IP                  |   Network
|-----------------------------------|
| DSL      802.11      Ethernet     |   Physical + data link 
+-----------------------------------+
Figura: Modelo da arquitetura TCP\IP

Entender os princípios dos processos de protocolo, entender as camadas de forma detalhada, sobre quais protocolos existem, e como isso funciona em uma questão de software e hardware. Será visto quais as diferenças de fibra, cabo trançado, fibra óptica, etc...
Como os dados navegam pela internet. Protocolos de wifi, etc...

Existem alguns bons programas para testar estes protocolos de forma prática, eles serão disponibilizados nas aulas.

Biografia:
-  Kevin R. Fall, W. Richard Stevens - TCP_IP Illustrated;
-  J.F. Kurose,  K.W. Ross - Computer networking_ A top-down approach;

