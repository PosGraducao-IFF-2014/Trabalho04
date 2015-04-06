from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
from flask_table import Table, Col
install(SQLitePlugin(dbfile='venda.sqlite'))

@post('/cadastra')
def venda_cadastro(db):
  codigo_venda = request.forms.get('codigo_venda')
  codigo_cliente = request.forms.get('codigo_cliente')
  codigo_funcionario = request.forms.get('codigo_funcionario')
  data = request.forms.get('data')
  valor_total = request.forms.get('valor_total')
  codigo_produto = request.forms.get('codigo_produto')
  quantidade = request.forms.get('quantidade')
  try:
    db.execute("INSERT INTO venda(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade) values ('%s' ,'%s', '%s', '%s', '%s', '%s', '%s')"%(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade)) 
    return '''<p>Cadastrada com Sucesso!!</p>'''
  except Exception, e:
    return e



run(reloader=True, host='localhost', port=8009, debug=True)
