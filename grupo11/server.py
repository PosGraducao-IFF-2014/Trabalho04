# -*- coding: utf-8 -*-
from bottle import route, run, template, post, request
from models import *
import ipdb

@post('/contas_a_receber')
def cria_conta_a_receber():
    ContaAReceber(request.json).salvar()

run(host='localhost', port=8011, debug=True)
