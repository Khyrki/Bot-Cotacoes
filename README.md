# Boas vindas ao repositório do projeto Bot-Cotações!


Aqui você vai encontrar os detalhes de como iniciar e entender o funcionamento da a aplicação que recebe dados de cotação de crypto moedas da API Poloniex, monta um objeto que representa um candle con dados de abertura, maxima, minima e fechamento e os salva em um banco de dados MySQL, usando python como linguagem de programação.

Para iniciar a aplicacao execute o comando:

`sudo docker-compose up -d`.

Com a aplicação rodando, a cada 1 minuto, 5 minutos e 10 minutos um novo candle será adicionando ao banco.
Você pode conferir os dados sendo escritos no banco acessando o container que esta rodando o MySQL seguindo os seguintes passos:

Escreva o comando `sudo docker ps` e identifique o container que está rodando o banco e copie o ID desse container.

![image](.imagens/exemplo1.png)

Com o ID execute o comando `docker exec -it (ID DO DOCNTAINER MySQL) bash` para ter acesso ao bash do container e por fim aos dados do banco:

Agora digite o comando `mysql -u root -p` no terminal, irá pedir uma senha, escreva "smarttbot" no campo e aperte enter, se tudo ocorrer bem vc tera acesso ao banco e ja pode fazer as consultas as tabelas que possuem as informações de cotação para cada intervalo de tempo:

![image](.imagens/exemplo2.png)

finalizado a consulta basta sair do mysql com o comando `exit` e do terminal do container tabém com o camndo `exit` e parar a aplicao com o comando `sudo docker-compose down`
