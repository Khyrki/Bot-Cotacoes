# biblioteca para fazer a conexao com o banco de dados
import mysql.connector

# Abrir uma conexao com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    port=3306,
    password='smarttbot',
    autocommit = True
)

# prepara um cursor para facilitar o envio de dados para o banco
cursor = conexao.cursor()
