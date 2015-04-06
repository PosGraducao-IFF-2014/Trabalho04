from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
import urllib
import json

@post('/cadastra_venda')
def venda(db):
  codigo_venda = request.forms.get('codigo_venda')
  codigo_cliente = request.forms.get('codigo_cliente')
  codigo_funcionario = request.forms.get('codigo_funcionario')
  data = request.forms.get('data')
  valor_total = request.forms.get('valor_total')
  codigo_produto = request.forms.get('codigo_produto')
  quantidade = request.forms.get('quantidade')
  db.execute("INSERT INTO venda(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade) values ('%s' ,'%s', '%s', '%s', '%s', '%s', '%s')"%(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade)) 
  print('Cadastrado!')

@get('/consulta/<post_id:int>')
def venda(db,post_id):
  response.content_type = 'application/json'
  v = db.execute('SELECT venda, codigo_venda FROM venda WHERE id = ?', (post_id))
  row = v.fetchone()
  return {'codigo_venda'}


run(reloader=True, host='localhost', port=8009, debug=True)