#Primeiro, vamos importar a biblioteca de sqlite, que iremos usar para o exercício
import sqlite3

#Usando a biblioteca, vamos criar as variáveis. Conexao vai dizer onde vai salvar. 
#bancoex é o nome do banco dentro do dbeaver, onde serão salvas as nossas tabelas
#Como estou salvando o banco e arquivo py na mesma pasta, não precisa de maiores orientacoes (como caminho da pasta)
conexao = sqlite3.connect('bancoex')
cursor = conexao.cursor()


#cursor.execute vai ser sempre onde vamos colocar os comandos do sql
#exercicio 6: Consultas e Funções Agregadas: Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dadosa = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for info in dadosa:
    print(info)

#b) Calcule o saldo médio dos clientes.
dadosb = cursor.execute('SELECT AVG(saldo) FROM clientes ')
for info in dadosb:
    print(info)

#c) Encontre o cliente com o saldo máximo.
dadosc = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')
for info in dadosc:
    print(info)
#d) Conte quantos clientes têm saldo acima de 1000
dadosd = cursor.execute('SELECT COUNT(*) AS total FROM clientes WHERE saldo>1000')
for info in dadosd:
    print(info)



#commit vai enviar os dados acima para o bd
conexao.commit()
#vai fechar a conexão feita para evitar problemas posteriores
conexao.close