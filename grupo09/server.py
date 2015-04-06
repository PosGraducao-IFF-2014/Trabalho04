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

@get('/consultaVenda')
def consulta_form():
    return '''  <h1>Consulta de Produto</h1></p>
                <form method="POST" action="/consultar">
                Codigo : <input name="codigo"     type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/consultar')
def consulta_submit(db):
  consulta_html ='''  <h1>Produto Consultado</h1></p>
                <form >
                    Codigo : {{codigo}}</p>
                    Descricao : {{descricao}}</p>
                    Preco : {{preco}}</p>
                    Codigo Fabricante : {{codigoFabricante}}</p>
                    <a href="/consultaProduto">Voltar</a></p>
                    <a href="/cadastraProduto">Cadastrar Novo Produto</a>
                </form>
                '''
  codigo     = request.forms.get('codigo_venda')
  try:
    c = db.execute('SELECT codigo_venda FROM venda WHERE codigo_venda = ?', (codigo_venda,))
    row = c.fetchone()
    return template(consulta_html, codigo_venda=row['codigo'], codigo_funcionario=row['descricao'])
  except Exception, e:
    return '''<p>Produto nao encontrado</p>'''

run(reloader=True, host='localhost', port=8009, debug=True)
