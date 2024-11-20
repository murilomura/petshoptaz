from flask import request, jsonify
from app.models.cliente import Cliente
from app import db

def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{"id": c.id, "nome": c.nome, "email": c.email} for c in clientes])

def adicionar_cliente():
    dados = request.json
    novo_cliente = Cliente(nome=dados['nome'], email=dados['email'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente adicionado com sucesso!"})
