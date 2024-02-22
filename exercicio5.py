#Primeiro, vamos importar a biblioteca de sqlite, que iremos usar para o exercício
import sqlite3

#Usando a biblioteca, vamos criar as variáveis. Conexao vai dizer onde vai salvar. 
#bancoex é o nome do banco dentro do dbeaver, onde serão salvas as nossas tabelas
#Como estou salvando o banco e arquivo py na mesma pasta, não precisa de maiores orientacoes (como caminho da pasta)
conexao = sqlite3.connect('bancoex')
cursor = conexao.cursor()


#cursor.execute vai ser sempre onde vamos colocar os comandos do sql
#exercicio 5: Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

#Insira algunsregistros de clientes na tabela
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1,"Davi", 58,1339.47)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2,"Arthur", 37,1257.83)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3,"Pedro", 66,79.92)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4,"Gabriel", 52,1079.95)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5,"Bernardo", 25,101.24)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6,"Lucas", 40,1114.60)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (7,"Matheus", 40,1148.55)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (8,"Rafael", 64,564.25)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (9,"Heitor", 70,132.47)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (10,"Enzo", 67,1465.77)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (11,"Guilherme", 64,1475.61)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (12,"Nicolas", 67,574.59)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (13,"Alice", 59,820.78)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (14,"Julia", 67,776.43)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (15,"Isabella", 56,1101.45)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (16,"Manuela", 44,1045.66)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (17,"Laura", 45,892.64)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (18,"Luiza", 50,517.16)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (19,"Valentina", 66,125.89)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (20,"Giovanna", 61,120.65)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (21,"Maria Eduarda", 20,167.48)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (22,"Helena", 19,286.98)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (23,"Beatriz", 39,1339.74)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (24,"Maria Luiza", 61,1405.39)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (25,"Lorenzo", 67,253.18)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (26,"Gustavo", 59,1086.91)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (27,"Felipe", 45,1386.93)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (28,"Lara", 24,48.76)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (29,"Mariana", 51,547.89)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (30,"Nicole", 24,659.29)')



#commit vai enviar os dados acima para o bd

conexao.commit()
#vai fechar a conexão feita para evitar problemas posteriores
conexao.close
