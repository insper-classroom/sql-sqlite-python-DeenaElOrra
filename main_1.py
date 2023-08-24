import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

#cursors allow us to process individual rowns by a query
# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnodeIngresso INTEGER
);
""")
          
estudantes = [
    ("Ana Silva", "Computação", 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alvez', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

# nome, curso... indica as colunas que os dados serao inseridos
# ? sao os tres valores que serao preenchidos para cada estudante
cursor.executemany(''' 
INSERT INTO Estudantes (Nome, Curso, AnodeIngresso) 
VALUES (?,?,?);                   
''', estudantes)

conn.commit()

#o execute nao retorna os resultados em si, ele apenas preprara a consulta SQL para ser buscado
cursor.execute("SELECT * FROM Estudantes")
# somente depois de execute voce ativamente visualiza os seus dados com os metodos fetchall, fetchmany, fetchone...

# fetchall mostra todos os registros requested pela consulta no execute
cursor.fetchall()

cursor.execute('SELECT Nome FROM Estudantes WHERE AnodeIngresso = 2019 OR AnodeIngresso = 2020')
cursor.fetchall()

# SET significa que voce deseja atualizar o valor de uma coluna para um novo valor. Com o WHERE, voce esta especificando qual a condicao que o ano de publicacao sera atualizado
cursor.execute("UPDATE Estudantes SET AnodeIngresso = ? WHERE Nome = ?", (2018,"Ana Silva"))
conn.commit()
# apos toda mudanca que fizer, voce deve dar o commit para salvar no banco de dados
# o ? eh um marcados de posicao para um valor que sera fornecido posteriormente 
cursor.execute("SELECT * FROM Estudantes")
cursor.fetchall()

# o execute precisa receber uma tupla como parametro sempre. Eh assim que a API esta definida. Por isso, mesmo que voce tenha apenas um parametro como argumento, voce passa (2,) com virgula para mostrar pro python que tem 2 argumentos.
cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (2,))
conn.commit()
cursor.execute("SELECT * FROM Estudantes")
cursor.fetchall()
# voce usa o fetchall quando, de fato, ha resultados para buscar. 
# o cursor.rowcount vai mostrar quantas linhas foram afetadas pela ultima alteracao, como DELETE, INSERT e UPDATE

cursor.execute("SELECT * FROM Estudantes WHERE Curso = ? AND AnodeIngresso > ?", ("Computação", 2019))
cursor.fetchall()

cursor.execute("UPDATE Estudantes SET AnodeIngresso = ? WHERE Curso = ?", (2018, "Computação"))
conn.commit()
cursor.rowcount
cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())
# rowcount nos notifica quantas linhas foram alteradas
# fetchall so funciona para metodos que fazem conjunto de dados a serem buscados


