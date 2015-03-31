# -*- coding: utf-8 -*-
import json
from bottle import run, post, get, delete, request, response, HTTPError, static_file
from models import *

@post('/contas_a_receber')
def cria_conta_a_receber():
    ContaAReceber(request.json).salvar()

@get('/contas_a_receber/<codigo>')
def retorna_conta_a_receber(codigo):
    return ContaAReceber.buscar(codigo) or HTTPError(status=404)

@delete('/contas_a_receber/<codigo>')
def retorna_conta_a_receber(codigo):
    ContaAReceber.buscar(codigo).remover()

@get('/contas_a_receber')
def retorna_conta_a_receber():
    response.content_type = 'application/json'
    return json.dumps(ContaAReceber.todas())

@get('/')
def index():
    return static_file('index.html', './client')

@get('/static/<filename>')
def server_static(filename):
        return static_file(filename, root='./client')

run(host='localhost', port=8011, debug=True)
