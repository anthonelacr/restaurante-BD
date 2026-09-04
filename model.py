import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cliente = """ 
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT NOT NULL
    );
"""

pedidos = '''
    CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    nome_prato TEXT NOT NULL,
    valor_unitario DOUBLE NOT NULL,
    qtd_pratos INTEGER NOT NULL,
    valor_total DOUBLE NOT NULL
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE
    );
    '''