from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
from flask_table import Table, Col
import urllib
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2




install(SQLitePlugin(dbfile='fabricante.sqlite'))


@route('/show/<post_id:int>')
def show(db, post_id):
    response.content_type = 'application/json'
    c = db.execute('SELECT codigo, nome, contato FROM fornecedor WHERE codigo = ?', (post_id,))
    row = c.fetchone()
    return {'codigo':row['codigo'], 'nome':row['nome']}


@get('/consultaFornecedor')
def consulta_form():
    return '''  <h1>Consulta de Fornecedor</h1></p>
                <form method="POST" action="/consultar">
                Codigo : <input name="codigo"     type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/consultar')
def consulta_submit(db):
    consulta_html ='''  <h1>Fornecedor Consultado</h1></p>
                <form >
                    Codigo : {{codigo}}</p>
                    Nome : {{nome}}</p>
                    Contato : {{contato}}</p>
                    <a href="/consultaFornecedor">Voltar</a></p>
                    <a href="/cadastraFornecedor">Cadastrar Novo Fornecedor</a>
                </form>
                '''
    codigo     = request.forms.get('codigo')
    try:
        c = db.execute('SELECT codigo, nome, contato FROM fornecedor WHERE codigo = ?', (codigo,))
        row = c.fetchone()
        return template(consulta_html, nome=row['nome'], codigo=row['codigo'], contato=row['contato'])
    except Exception, e:
        return '''<p>Fornecedor nao encontrado</p>
                      <a href="/consultaFornecedor">Voltar</a></p>
                      <a href="/cadastraFornecedor">Cadastrar Novo Fornecedor</a>
        '''

@get('/cadastraFornecedor')
def cadastro_form():
    return '''  <h1>Cadastro de Fornecedor</h1></p>
                <form method="POST" action="/cadastrar">
                Codigo : <input name="codigo"     type="text" /></p>
                Nome : <input name="nome"     type="text" /></p>
                Contato : <input name="contato"     type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/cadastrar')
def cadastrar_submit(db):
    codigo     = request.forms.get('codigo')
    nome     = request.forms.get('nome')
    contato     = request.forms.get('contato')
    try:
        db.execute("INSERT INTO fornecedor (codigo, nome, contato ) values ('%s', '%s', '%s')"%(codigo, nome, contato))
        return '''<p>Fornecedor Cadastrado com Sucesso</p>
                    <a href="/consultaFornecedor">Consultar Fornecedor</a></p>
                    <a href="/cadastraFornecedor">Cadastrar Novo Fornecedor</a>
                    '''
    except Exception, e:
        return '''<p>Erro ao cadastrar Fornecedor</p>
                     <a href="/cadastraFornecedor">Voltar</a>
        '''


@get('/deletarFornecedor')
def deletar_form():
    return '''  <h1>Exclusao de Fornecedor</h1></p>
                <form method="POST" action="/deletar">
                Codigo : <input name="codigo"     type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/deletar')
def deletar_submit(db):
    codigo     = request.forms.get('codigo')
    try:
        if fornecedorPodeSerDeletado (codigo):
            db.execute('DELETE FROM fornecedor WHERE codigo = ?', (codigo,))
            return '''<p>Fornecedor Deletado com Sucesso</p>
                    <a href="/consultaFornecedor">Consultar Fornecedor</a></p>
                    <a href="/cadastraFornecedor">Cadastrar Novo Fornecedor</a></p>
                    <a href="/deletarFornecedor">Deletar Fornecedor</a>
                    '''
        else:
            return "<p>Fornecedor nao pode ser deletado pois existe Compra vinculada</p>"
    except Exception, e:
        return "<p>Erro ao deletar Fornecedor</p>"

def fornecedorPodeSerDeletado(codigo):
    url = "http://localhost:8007/existe/"+str(codigo)
    request = urllib2.Request(url)
    fd = urllib2.urlopen(request,timeout=2)
    content =  fd.readlines()
    fd.close()
    if content ==[]:
        return True
    else:
        return False



@get('/listarFornecedor')
def listar_fornecedores(db):
    try:
        c = db.execute('SELECT codigo, nome, contato FROM fornecedor')
        result = c.fetchall()
        #montar lista de itens
        items = []
        for row in result:
            items.append(Item(row['codigo'],row['nome'],row['contato']))

        table = ItemTable(items)
        return table.__html__()
    except Exception, e:
        return "<p>Erro ao listar Fornecedores</p>"



class ItemTable(Table):
    codigo = Col('Codigo')
    nome = Col('Nome')
    contato = Col('Contato')

class Item(object):
    def __init__(self, codigo, nome, contato):
        self.codigo = codigo
        self.nome = nome
        self.contato = contato



run(reloader=True, host='localhost', port=8005,debug=True)