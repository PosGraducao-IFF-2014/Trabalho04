# -*- coding: utf-8 -*-
import json, requests
from bottle import run, post, get, delete, request, response, HTTPError, \
    static_file, install, redirect, template
from models import *

from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='db.sqlite'))

def estoque_existe(codigo_estoque):
    #resposta = requests.get('localhost:8001/estoque/'+codigo_estoque)
    #return resposta.json
    #return {'codigo': 1, 'descricao': 'caneta bic', 'localizacao': 'campos'}
    return {}

def produto_existe(codigo_produto):
    #resposta = requests.get('localhost:8003/produto/'+codigo_produto)
    #return resposta.json
    #return {'codigo': 1, 'descricao': 'caneta bic', 'preco': 4, 'codigo_fabricante': 1}
    return {}

@post('/produto_estoque')
def inserir_produto_estoque(db):
    codigo_estoque = request.forms.get('codigo_estoque')
    codigo_produto = request.forms.get('codigo_produto')
    quantidade = request.forms.get('quantidade')

    if produto_existe(codigo_produto) and estoque_existe(codigo_estoque):
        db.execute("""
        insert into produto_estoque(codigo_estoque, codigo_produto, quantidade)
        values (%s, %s, %s)
        """ % (codigo_estoque, codigo_produto, quantidade,))
        redirect('/')
    else:
        queryset = db.execute("""
            select * from produto_estoque
        """)
        produtos_estoques = map(lambda row: dict(zip(row.keys(), row)), queryset)
        return template('index', erro='Código ou Estoque não existente!',
            produtos_estoques=produtos_estoques)

@get('/consulta_produto_em_estoque/<codigo_produto>')
def consulta_produto(db, codigo_produto):
    total = db.execute("""
    select count(*) as total from produto_estoque
    where codigo_produto = %s""" % (codigo_produto,)).fetchone()['total']
    return '1' if total > 0 else '0'

@get('/consulta_estoque_em_produto_estoque/<codigo_estoque>')
def consulta_estoque(db, codigo_estoque):
    total = db.execute("""
    select count(*) as total from produto_estoque
    where codigo_estoque = %s""" % (codigo_estoque,)).fetchone()['total']
    return '1' if total > 0 else '0'

@get('/consulta_preco_em_produto_estoque')
def consulta_preco_em_produto_estoque(db):
    codigo_produto = request.params.get('codigo_produto')
    resposta = request.get('localhost:8003/consulta_produto/'+codigo_produto)
    return resposta.json['preco']

@get('/')
def index(db):
    queryset = db.execute("""
        select * from produto_estoque
    """)
    produtos_estoques = map(lambda row: dict(zip(row.keys(), row)), queryset)
    return template('index', produtos_estoques=produtos_estoques, erro=None)

run(host='localhost', port=8004, debug=True)
