#Primeiro, vamos importar a biblioteca de sqlite, que iremos usar para o exercício
import sqlite3

#Usando a biblioteca, vamos criar as variáveis. Conexao vai dizer onde vai salvar. 
#bancoex é o nome do banco dentro do dbeaver, onde serão salvas as nossas tabelas
#Como estou salvando o banco e arquivo py na mesma pasta, não precisa de maiores orientacoes (como caminho da pasta)
conexao = sqlite3.connect('bancoex')
cursor = conexao.cursor()


#cursor.execute vai ser sempre onde vamos colocar os comandos do sql
#exercicio 4: Atualização e Remoção:
#a)  Atualize a idade de um aluno específico na tabela
cursor.execute('UPDATE alunos SET idade=27 WHERE ID=5')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE ID = 5')



#commit vai enviar os dados acima para o bd
conexao.commit()
#vai fechar a conexão feita para evitar problemas posteriores
conexao.close