from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
from flask_table import Table, Col
import urllib
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2

install(SQLitePlugin(db='fabricante.db'))

@get('/cadastraFabricante')
def cadastro_form():
    return '''  <h1>Cadastro de Fabricante</h1></p>
                <form method="POST" action="/cadastrarFabricante">
                Codigo : <input name="codigo" type="text" /></p>
                Descricao : <input name="descricao" type="text" /></p>
                Localizacao : <input name="localizacao" type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/cadastrarFabricante')
def cadastraFabricante(db):
    codigo = request.forms.get('codigo')
    descricao = request.forms.get('descricao')
    localizacao = request.forms.get('localizacao')
    try:
        db.execute("INSERT INTO fabricante (codigo, descricao, localizacao) values ('%s', '%s', '%s')" %(codigo, descricao, localizacao))
        return '''<p>Fabricante Cadastrado com Sucesso</p>
                    <a href="/consultaFabricante">Consultar Fabricante</a></p>
                    <a href="/cadastraFabricante">Cadastrar Fabricante</a>
                    '''
    except Exception, e:
        return '''<p>Erro ao cadastrar Fabricante</p>
                     <a href="/cadastraFabricante">Voltar</a>
        '''

@get('/consultaFabricante')
def consultaFabricante():
    return '''  <h1>Consulta de Fabricante</h1></p>
                <form method="POST" action="/consultar">
                Codigo : <input name="codigo" type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/consultarFabricante')
def consultarFabricante(db):
    consulta_html ='''  <h1>Fabricante</h1></p>
                <form >
                    Codigo : {{codigo}}</p>
                    Descricao : {{descricao}}</p>
                    Localizacao : {{localizacao}}</p>
                    <a href="/consultaFabricante">Voltar</a></p>
                    <a href="/cadastraFabricante">Cadastrar Fabricante</a>
                </form>
                '''
    codigo = request.forms.get('codigo')
    try:
        c = db.execute('SELECT codigo, descricao, localizacao FROM fabricante WHERE codigo = ?', (codigo))
        row = c.fetchone()
        return template(consulta_html, codigo=row['codigo'], descricao=row['descricao'], localizacao=row['localizacao'])
    except Exception, e:
        return '''<p>Fabricante nao encontrado</p>
                      <a href="/consultaFabricante">Voltar</a></p>
                      <a href="/cadastraFabricante">Cadastrar Fabricante</a>
        '''

@get('/deletaFabricante')
def deletaFabricante():
    return '''  <h1>Exclusao de Fabricante</h1></p>
                <form method="POST" action="/deletar">
                Codigo: <input name="codigo" type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/deletarFabricante')
def deletarFabricante(db):
    codigo = request.forms.get('codigo')
    try:

        url = "http://localhost:8003/listarProduto/"
        request = urllib2.Request(url)

        fd = urllib2.urlopen(request,timeout=2)

        content =  fd.readlines()

        fd.close()

        existe = False

        for linha in content:
            codigo, descricao, preco, codigoFabricante = linha.split('|')
            if id == codigoFabricante:
                existe = True

        if existe is False:
            db.execute('DELETE FROM fabricante where id = ?', id)
            return '''<p>Fabricante deletado com Sucesso</p>
                        <a href="/consultaFabricante">Consultar Fabricante</a></p>
                        <a href="/cadastraFabricante">Cadastrar Fabricante</a></p>
                        <a href="/deletaFabricante">Deletar Fabricante</a>
                        '''
        else:
            return '''<p>N&atilde;o foi poss&iacute;vel excluir o fabricante.</p>'''

    except Exception, e:
        return "<p>Erro ao deletar fabricante</p>"

@get('/listaFabricante')
def listaFabricante(db):
    try:
        c = db.execute('SELECT codigo, descricao, localizacao, FROM fabricante')
        result = c.fetchall()

        items = []
        for row in result:
            items.append(Item(row['codigo'],row['descricao'],row['localizacao']))

        table = ItemTable(items)

        return table.__html__()
    except Exception, e:
        return "<p>Erro ao listar Fabricante</p>"

class ItemTable(Table):
    codigo = Col('codigo')
    descricao = Col('descricao')
    localizacao = Col('localizacao')

class Item(object):
    def __init__(self, codigo, descricao, localizacao):
        self.codigo = codigo
        self.descricao = descricao
        self.localizacao = localizacao

run(reloader=True, host='localhost', port=8002, debug=True)
