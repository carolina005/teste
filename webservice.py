from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_hamburguer_names(self):
        self.cursor.execute("SELECT nome_hamburguer FROM Hamburguer")
        return [row[0] for row in self.cursor.fetchall()]

    def insert_order(self, nome, morada, telefone, hamburguer, quantidade, tamanho, valor_total):
        self.cursor.execute("INSERT INTO Cliente (nome, morada, telefone) VALUES (?, ?, ?)", (nome, morada, telefone))
        id_cliente = self.cursor.lastrowid
        self.cursor.execute("""
            INSERT INTO Pedido (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total)
            VALUES (?, ?, ?, ?, ?)
        """, (id_cliente, hamburguer, quantidade, tamanho, valor_total))
        self.conn.commit()

db = Database('callcenter.db')

@app.route('/hamburgers', methods=['GET'])
def get_hamburgers():
    hamburgers = db.get_hamburguer_names()
    return jsonify(hamburgers)

@app.route('/order', methods=['POST'])
def make_order():
    data = request.json
    db.insert_order(
        data['nome'], data['morada'], data['telefone'],
        data['hamburguer'], data['quantidade'], data['tamanho'], data['valor_total']
    )
    return jsonify({'message': 'Pedido realizado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
