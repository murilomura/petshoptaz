from flask import request, jsonify
from app.models.produto import Produto
from app import db

def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{"id": p.id, "nome": p.nome, "preco": p.preco, "estoque": p.estoque} for p in produtos])

def adicionar_produto():
    dados = request.json
    novo_produto = Produto(nome=dados['nome'], preco=dados['preco'], estoque=dados['estoque'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({"message": "Produto adicionado com sucesso!"})
