from flask import request, jsonify
from app.models.pedido import Pedido
from app import db

def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{"id": p.id, "cliente_id": p.cliente_id, "produto_id": p.produto_id, "quantidade": p.quantidade, "total": p.total} for p in pedidos])

def adicionar_pedido():
    dados = request.json
    novo_pedido = Pedido(cliente_id=dados['cliente_id'], produto_id=dados['produto_id'], quantidade=dados['quantidade'], total=dados['total'])
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({"message": "Pedido adicionado com sucesso!"})
