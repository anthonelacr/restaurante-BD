import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cliente = """ 
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT NOT NULL
    );
"""