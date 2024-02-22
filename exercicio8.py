#Primeiro, vamos importar a biblioteca de sqlite, que iremos usar para o exercício
import sqlite3

#Usando a biblioteca, vamos criar as variáveis. Conexao vai dizer onde vai salvar. 
#bancoex é o nome do banco dentro do dbeaver, onde serão salvas as nossas tabelas
#Como estou salvando o banco e arquivo py na mesma pasta, não precisa de maiores orientacoes (como caminho da pasta)
conexao = sqlite3.connect('bancoex')
cursor = conexao.cursor()


#cursor.execute vai ser sempre onde vamos colocar os comandos do sql
#exercicio 8: 8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, client_id INT,  produto VARCHAR(100), valor FLOAT, CONSTRAINT fk_pessoacompra FOREIGN KEY (client_id) REFERENCES clientes (id))')


#Insira algumas compras associadas a clientes existentes na tabela "clientes".
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (1,33,"Caneta",41.95)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (2,22,"Caderno",10.63)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (3,31,"Lápis",1.11)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (4,31,"Borracha",16.48)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (5,23,"Livro",42.68)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (6,34,"Caneta",18.64)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (7,38,"Caderno",2.84)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (8,12,"Caneta",3.40)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (9,39,"Caderno",44.77)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (10,9,"Lápis",0.86)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (11,34,"Borracha",42.34)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (12,35,"Livro",24.92)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (13,30,"Caneta",22.25)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (14,6,"Caderno",8.34)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (15,38,"Caneta",15.58)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (16,38,"Caderno",36.26)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (17,16,"Lápis",49.41)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (18,8,"Borracha",48.24)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (19,25,"Livro",27.41)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (20,22,"Caneta",31.32)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (21,5,"Caderno",45.78)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (22,37,"Caneta",0.14)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (23,21,"Caderno",35.97)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (24,11,"Lápis",32.33)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (25,40,"Borracha",33.42)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (26,38,"Livro",40.26)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (27,1,"Caneta",17.34)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (28,21,"Caderno",17.52)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (29,4,"Lápis",2.58)')
cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES (30,5,"Borracha",23.61)')


#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
dados = cursor.execute('SELECT nome, produto, valor FROM compras LEFT JOIN clientes ON compras.client_id =  clientes.id')
for info in dados:
    print(info)


#commit vai enviar os dados acima para o bd

conexao.commit()
#vai fechar a conexão feita para evitar problemas posteriores
conexao.close
