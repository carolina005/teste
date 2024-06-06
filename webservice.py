# app.py (Web Service Flask)
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'callcenter.db'


def execute_query(query, args=()):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
        return cursor.lastrowid


def query_db(query, args=(), one=False):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        rv = cursor.fetchall()
        return (rv[0] if rv else None) if one else rv


@app.route('/')
def index():
    return "Web Service Flask está funcionando!", 200


@app.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.json
    query = "INSERT INTO Cliente (nome, morada, telefone) VALUES (?, ?, ?)"
    id_cliente = execute_query(query, (data['nome'], data['morada'], data['telefone']))
    return jsonify({'id_cliente': id_cliente}), 201


@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = query_db("SELECT * FROM Cliente")
    return jsonify(clientes), 200


@app.route('/hamburgueres', methods=['POST'])
def add_hamburguer():
    data = request.json
    query = "INSERT INTO Hamburguer (nome_hamburguer, ingredientes) VALUES (?, ?)"
    execute_query(query, (data['nome_hamburguer'], data['ingredientes']))
    return jsonify({'nome_hamburguer': data['nome_hamburguer']}), 201


@app.route('/hamburgueres', methods=['GET'])
def get_hamburgueres():
    hamburgueres = query_db("SELECT * FROM Hamburguer")
    return jsonify(hamburgueres), 200


@app.route('/pedidos', methods=['POST'])
def add_pedido():
    data = request.json
    query = """
    INSERT INTO Pedido (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total) 
    VALUES (?, ?, ?, ?, ?)
    """
    id_pedido = execute_query(query, (data['id_cliente'], data['nome_hamburguer'], data['quantidade'], data['tamanho'], data['valor_total']))
    return jsonify({'id_pedido': id_pedido}), 201


@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    pedidos = query_db("SELECT * FROM Pedido")
    return jsonify(pedidos), 200


if __name__ == '__main__':
    app.run(debug=True)
