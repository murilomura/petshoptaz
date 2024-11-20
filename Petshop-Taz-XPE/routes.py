from flask import Blueprint
from app.controllers.produtos_controller import listar_produtos, adicionar_produto
from app.controllers.clientes_controller import listar_clientes, adicionar_cliente
from app.controllers.pedidos_controller import listar_pedidos, adicionar_pedido

def configure_routes(app):
    # Produtos
    app.add_url_rule('/produtos', 'listar_produtos', listar_produtos, methods=['GET'])
    app.add_url_rule('/produtos', 'adicionar_produto', adicionar_produto, methods=['POST'])

    # Clientes
    app.add_url_rule('/clientes', 'listar_clientes', listar_clientes, methods=['GET'])
    app.add_url_rule('/clientes', 'adicionar_cliente', adicionar_cliente, methods=['POST'])

    # Pedidos
    app.add_url_rule('/pedidos', 'listar_pedidos', listar_pedidos, methods=['GET'])
    app.add_url_rule('/pedidos', 'adicionar_pedido', adicionar_pedido, methods=['POST'])
