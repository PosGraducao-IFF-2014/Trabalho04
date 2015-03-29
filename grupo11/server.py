# -*- coding: utf-8 -*-
import json
from bottle import route, run, template, post, get, request, response, HTTPError
from models import *
import ipdb

@post('/contas_a_receber')
def cria_conta_a_receber():
    ContaAReceber(request.json).salvar()

@get('/contas_a_receber/<codigo_conta>')
def retorna_conta_a_receber(codigo_conta):
    response.content_type = 'application/json'
    try:
        return json.dumps(ContaAReceber.buscar_por_codigo(codigo_conta))
    except IndexError:
        return HTTPError(status=404)

run(host='localhost', port=8011, debug=True)
