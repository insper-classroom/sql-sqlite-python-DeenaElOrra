import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

def criar_tabela(nome_tabela, nome_estudante, curso, anodeingresso):
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    {nome_estudante} TEXT NOT NULL,
    {curso} TEXT NOT NULL,
    {anodeingresso} INTEGER
);
""")
    conn.commit()

estudantes = [
    ("Ana Silva", "Computação", 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alvez', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

def inserir_dados(nome_tabela, nome_estudantes, curso, AnodeIngresso, lista_de_dados):
    cursor.executemany(f''' 
    INSERT INTO {nome_tabela} ({nome_estudantes}, {curso}, {AnodeIngresso}) 
    VALUES (?,?,?);                   
    ''', lista_de_dados)

    conn.commit()

def consultar_registro(nome_tabela):
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    cursor.fetchall()

def atualizar_dados(nome_tabela, coluna_AnodeIngresso, nome, ano, nome_estudante):
    cursor.execute(f"UPDATE {nome_tabela} SET {coluna_AnodeIngresso} = ? WHERE {nome} = ?", (ano,f"{nome_estudante}"))
    conn.commit()

def deletar(nome_tabela, num_id):
    cursor.execute(f"DELETE FROM {nome_tabela} WHERE ID = ?", (num_id,))
    conn.commit()


