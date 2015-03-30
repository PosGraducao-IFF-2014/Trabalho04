# -*- coding: utf-8 -*-
import json
from bottle import run, post, get, delete, request, response, HTTPError
from models import *
import ipdb

@post('/contas_a_receber')
def cria_conta_a_receber():
    ContaAReceber(request.json).salvar()

@get('/contas_a_receber/<codigo_conta>')
def retorna_conta_a_receber(codigo_conta):
    conta_a_receber = ContaAReceber.buscar_por_codigo(codigo_conta)
    return conta_a_receber or HTTPError(status=404)

@delete('/contas_a_receber/<codigo_conta>')
def retorna_conta_a_receber(codigo_conta):
    ContaAReceber.buscar_por_codigo(codigo_conta).remover()

run(host='localhost', port=8011, debug=True)
