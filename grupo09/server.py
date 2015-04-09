from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
import json

install(SQLitePlugin(dbfile='venda.sqlite'))
#----------------------------------------------------------------------------------
@get('/cadastra_venda')
def html_():
    return '''  
      <h1>Cadastro de Venda</h1></p>
      <form class="form-group" method="POST" action="/cadastra"><br>
        <label>Codigo Venda: <input type="text" class="form-control" name="codigo_venda"><br>
        <label>Codigo Cliente: <input type="text" class="form-control" name="codigo_cliente" ><br>
        <label>Codigo Funcionario: <input type="text" class="form-control" name="codigo_funcionario" ><br>
        <label>Data: <input type="text" class="form-control"  name="data" ><br>
        <label>Valor Total: <input type="text" class="form-control"  name="valor_total" ><br>
        <label>Codigo Produto:<input type="text" class="form-control" name="codigo_produto" >  <br>
        <label>Quantidade:<input type="text" class="form-control" name="quantidade" > <br>
        <button type="submit" class="btn btn-xm btn-info">Cadastrar</button>            
      </form>'''

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
    db.execute("INSERT INTO venda(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade)) 
    return '''<p>Cadastrada com Sucesso!!</p>'''
  except Exception, e:
    return e
#---------------------------------------------------------------------------------
@get('/consulta_venda')
def html_():
    return ''' 
    <h3>Consulta de Venda</h3></p>
    <form method="POST" action="/consulta">
      Codigo : <input name="codigo_venda"     type="text" /></p>
      <input type="submit" />
    </form>'''

@post('/consulta')
def venda_consulta(db):
  html_ = ''' 
    Codigo Venda: {{codigo_venda}}           
    Codigo Cliente: {{codigo_cliente}}
    Codigo Funcionario: {{codigo_funcionario}}
    Valor Total:{{valor_total}}
    Codigo Produto:{{codigo_produto}}
    '''
  codigo_venda = request.forms.get('codigo_venda')
  try:    
    response.content_type = 'application/json'
    v = db.execute('SELECT codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade FROM venda WHERE codigo_venda = ?', (codigo_venda))
    row = v.fetchone()
    return template(html_, codigo_venda=row['codigo_venda'], codigo_cliente=row['codigo_cliente'], codigo_funcionario=row['codigo_funcionario'], valor_total=row['valor_total'], codigo_produto=row['codigo_produto'])
  except Exception, e:
    return "Venda ID nao encontrada!"
#---------------------------------------------------------------------------------
@get('/deleta_venda')
def html_():
    return '''  
      <h1>Exclusao de Venda</h1></p>
      <form method="POST" action="/deleta">
          Codigo Venda : <input name="codigo_venda"     type="text" /></p>
          <input type="submit" />
      </form>'''

@post('/deleta')
def venda_deleta(db):
    codigo_venda = request.forms.get('codigo_venda')
    try:
      if existe(db, codigo_venda):
        db.execute('DELETE FROM venda WHERE codigo_venda = ?', (codigo_venda))
        return 'Venda Deletada '
      else:
        return 'Nao foi possivel excluir .'

    except Exception, e:
        return 'Venda ID nao encontrada!'
#---------------------------------------------------------------------------------  
@route('/existe/<post_id:int>')
def existe(db, post_id):
  response.content_type = 'application/json'
  v = db.execute('SELECT codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade FROM venda  WHERE codigo_venda = ?', (post_id,))
  row = v.fetchone()
  if row==None:
    return 'Nao foram encontradas vendas com esse ID'
  else:
    return {'codigo_venda':row['codigo_venda'], 'codigo_cliente':row['codigo_cliente'], 'codigo_funcionario':row['codigo_funcionario'], 'valor_total':row['valor_total'], 'codigo_produto':row['codigo_produto']}

#---------------------------------------------------------------------------------
#Method to group 8
@get('/existe_venda_por_funcionario/<post_id:int>')
def existe(db, post_id):
  response.content_type = 'application/json'
  v = db.execute('SELECT codigo_funcionario FROM venda  WHERE codigo_funcionario = ?', (post_id))
  row = v.fetchone()
  if row==None:
    return False
  else:
    return True

#----------------------------------------------------------------------------------
run(reloader=True, host='localhost', port=8009, debug=True)