#Primeiro, vamos importar a biblioteca de sqlite, que iremos usar para o exercício
import sqlite3

#Usando a biblioteca, vamos criar as variáveis. Conexao vai dizer onde vai salvar. 
#bancoex é o nome do banco dentro do dbeaver, onde serão salvas as nossas tabelas
#Como estou salvando o banco e arquivo py na mesma pasta, não precisa de maiores orientacoes (como caminho da pasta)
conexao = sqlite3.connect('bancoex')
cursor = conexao.cursor()


#cursor.execute vai ser sempre onde vamos colocar os comandos do sql
#exercicio 2: insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Faq", 35, "Letras")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Himi", 28, "Música")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Funko", 18, "Artes")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Fiona", 18, "Letras")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Oreo", 30, "Geografia")')


#commit vai enviar os dados acima para o bd

conexao.commit()
#vai fechar a conexão feita para evitar problemas posteriores
conexao.close
