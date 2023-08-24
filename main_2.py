import sqlite3
import  db.db_utils as db_utils 

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

tabela = db_utils.criar_tabela('Estudantes', 'Nome', 'Curso', 'AnodeIngresso')

estudantes = [
    ("Ana Silva", "Computação", 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alvez', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

insercao_de_dados = db_utils.inserir_dados('Estudantes', 'Nome', 'Curso', 'AnodeIngresso', estudantes)

consultar_dados = db_utils.consultar_registro('Estudantes')

atualizar_dados = db_utils.atualizar_dados('Estudantes', 'AnodeIngresso', 'Nome', 2018, 'Ana Silva')

deletar_dados = db_utils.deletar('Estudantes', 2)