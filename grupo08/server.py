from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
import json

install(SQLitePlugin(dbfile='funcionario.sqlite'))

@get('/cadastra_funcionario')
def html_():
    return '''<h1>Cadastro de Funcionario</h1></p>
      <form class="form-group" method="POST" action="/cadastra"><br>
        <label>Codigo Funcionario: <input type="text" class="form-control" name="codigo_funcionario"><br>
        <label>Nome Funcionario: <input type="text" class="form-control" name="nome_funcionario" ><br>
        <label>Endereco Funcionario: <input type="text" class="form-control" name="endereco_funcionario" ><br>
        <label>Sexo Funcionario: <input type="text" class="form-control"  name="sexo_funcionario" ><br>
        <label>Datanascimento Funcionario: <input type="text" class="form-control"  name="datanascimento_funcionario" ><br>
        <button type="submit" class="btn btn-xm btn-info">Cadastrar</button>            
      </form>'''

@post('/cadastra')
def funcionario_cadastro(db):
  codigo_funcionario = request.forms.get('codigo_funcionario')
  nome_funcionario = request.forms.get('nome_funcionario')
  endereco_funcionario = request.forms.get('endereco_funcionario')
  sexo_funcionario = request.forms.get('sexo_funcionario')
  datanascimento_funcionario = request.forms.get('datanascimento_funcionario')
  try:
    db.execute("INSERT INTO funcionario(codigo_funcionario,nome_funcionario,endereco_funcionario,sexo_funcionario,datanascimento_funcionario) values ('%s', '%s', '%s', '%s', '%s')" %(codigo_funcionario,nome_funcionario,endereco_funcionario,sexo_funcionario,datanascimento_funcionario)) 
    return '''#<p>Cadastrada com Sucesso!!</p>'''
  except Exception, e:
    return e

@get('/consulta_funcionario')
def html_():
    return '''
    <h3>Consulta de Funcionario</h3></p>
    <form method="POST" action="/consulta">
      Codigo : <input name="codigo_funcionario"     type="text" /></p>
      <input type="submit" />
    </form>'''

@post('/consulta')
def funcionario_consulta(db):
  html_ = '''
     Codigo Funcionario: {{codigo_funcionario}}           
     Nome Funcionario {{nome_funcionario}}
     Sexo Funcionario: {{sexo_funcionario}}
     Datanascimento Funcionario:{{datanascimento_funcionario}}
     '''
  codigo_funcionario = request.forms.get('codigo_funcionario')
  try:    
    response.content_type = 'application/json'
    v = db.execute('SELECT codigo_funcionario, nome_funcionario,sexo_funcionario,datanascimento_funcionario FROM funcionario WHERE codigo_funcionario = ?', (codigo_funcionario))
    row = v.fetchone()
    return template(html_, codigo_funcionario=row['codigo_funcionario'], nome_funcionario=row['nome_funcionario'], sexo_funcionario=row['sexo_funcionario'], datanascimento_funcionario=row['datanascimento_funcionario'])
  except Exception, e:
    return "Codigo do funcionario nao encontrada!"

#-----------------------Deletar Funcionario---------------------------------

@get('/deleta_funcionario')
def html_():
    return '''  
      <h1>Exclusao de Funcionario</h1></p>
      <form method="POST" action="/deleta">
        Codigo funcionario : <input name="codigo_funcionario" type="text" /></p>
        <input type="submit" />
      </form>'''

@post('/deleta')
def venda_deleta(db):
    codigo_funcionario = request.forms.get('codigo_funcionario')
    try:
      if existe(db, codigo_funcionario):
        db.execute('DELETE FROM funcionario WHERE codigo_funcionario = ?', (codigo_funcionario))
        return 'Funcionario Deletado '
      else:
        return 'Nao foi possivel excluir o funcionario .'

    except Exception, e:
        return "Nao encontrado" 

#------------------------------------------------
@route('/existe/<post_id:int>')
def existe(db, post_id):
  response.content_type = 'application/json'
  v = db.execute('SELECT codigo_funcionario FROM funcionario  WHERE codigo_funcionario = ?', (post_id,))
  row = v.fetchone()
  if row==None:
    return 'Nao foram encontrados funcionarios com esse codigo'
  else:
    return {'codigo_funcionario':row['codigo_funcionario']}


#----------------------------------------------------------------------------------
run(reloader=True, host='localhost', port=8008, debug=True)


