import sqlite3

sql = """
CREATE TABLE
    Cliente (
        id_cliente INTEGER CONSTRAINT Cliente_pk PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        morada TEXT NOT NULL,
        telefone TEXT NOT NULL
    );

CREATE TABLE
    Hamburguer (
        nome_hamburguer TEXT CONSTRAINT Hamburguer_pk PRIMARY KEY,
        ingredientes TEXT NOT NULL
    );

CREATE TABLE
    Pedido (
        id_pedido INTEGER CONSTRAINT Pedido_pk PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL CONSTRAINT Pedido_Cliente_id_cliente_fk REFERENCES Cliente(id_cliente) ON UPDATE CASCADE ON DELETE CASCADE,
        nome_hamburguer TEXT NOT NULL CONSTRAINT Pedido_Hamburguer_nome_hamburguer_fk REFERENCES Hamburguer(nome_hamburguer) ON UPDATE CASCADE ON DELETE CASCADE,
        quantidade INTEGER NOT NULL,
        tamanho TEXT NOT NULL CHECK(tamanho IN ('infantil', 'normal', 'duplo')),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        valor_total REAL NOT NULL
    );
"""

with sqlite3.connect("callcenter.db") as conn:
    cursor = conn.cursor()
    cursor.executescript(sql)
