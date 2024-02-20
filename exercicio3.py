#Primeiro, vamos importar a biblioteca de sqlite, que iremos usar para o exercício
import sqlite3

#Usando a biblioteca, vamos criar as variáveis. Conexao vai dizer onde vai salvar. 
#bancoex é o nome do banco dentro do dbeaver, onde serão salvas as nossas tabelas
#Como estou salvando o banco e arquivo py na mesma pasta, não precisa de maiores orientacoes (como caminho da pasta)
conexao = sqlite3.connect('bancoex')
cursor = conexao.cursor()


#cursor.execute vai ser sempre onde vamos colocar os comandos do sql
#exercicio 3: Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dadosa = cursor.execute('SELECT * FROM alunos')
for info in dadosa:
    print(info)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dadosb = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for info in dadosb:
    print(info)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dadosc = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" order by nome')
for info in dadosc:
    print(info)
#d) Contar o número total de alunos na tabela
dadosd = cursor.execute('SELECT COUNT(*) AS total FROM alunos')
for info in dadosd:
    print(info)



#commit vai enviar os dados acima para o bd
conexao.commit()
#vai fechar a conexão feita para evitar problemas posteriores
conexao.close
