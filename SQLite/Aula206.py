# Entendendo como funciona o SQLite

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Apaga todos os registros da tabela
# cursor.execute("DELETE FROM customers")
# connection.commit()  # Finaliza a transação antes do VACUUM

# Executa VACUUM para resetar IDs e liberar espaço/ O VACUUM reorganiza o banco de dados e não pode ser executado dentro de uma transação aberta.
# connection.execute("VACUUM")
# connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'Name TEXT,'
    'Weight REAL'
    ')'
)


# Deleta e reseta o registro no banco de dados
# connection.commit()

# cursor.execute(f"DELETE FROM {TABLE_NAME}")
# connection.commit()  # Finaliza a transação antes do VACUUM
 
# connection.execute("VACUUM") VACUUM no SQLite é usado para reorganizar o banco de dados e liberar espaço não utilizado após operações de exclusão.
# connection.commit()



# Registra valores nas colunas da tabela
NAME = input('Digite o seu nome: ')
WEIGHT = float(input('Digite o seu peso: '))

# Inserir dados na tabela
cursor.execute("INSERT INTO customers (NAME, WEIGHT) VALUES(?, ?)",(NAME, WEIGHT))
connection.commit()

print('Dados inseridos com sucesso!')


# Fechar conexão
cursor.close()
connection.close()