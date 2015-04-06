from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
from flask_table import Table, Col



install(SQLitePlugin(dbfile='produtos.sqlite'))


@route('/show/<post_id:int>')
def show(db, post_id):
    response.content_type = 'application/json'
    c = db.execute('SELECT codigo,descricao,preco, codigoFabricante FROM produtos WHERE codigo = ?', (post_id,))
    row = c.fetchone()
    return {'codigo':row['codigo'], 'descricao':row['descricao'], 'preco':row['preco'], 'codigoFabricante':row['codigoFabricante']}


@get('/consultaProduto')
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
    codigo     = request.forms.get('codigo')
    try:
        c = db.execute('SELECT codigo,descricao,preco, codigoFabricante FROM produtos WHERE codigo = ?', (codigo,))
        row = c.fetchone()
        return template(consulta_html, codigo=row['codigo'], descricao=row['descricao'], preco=row['preco'], codigoFabricante=row['codigoFabricante'])
    except Exception, e:
        return '''<p>Produto nao encontrado</p>
                      <a href="/consultaProduto">Voltar</a></p>
                      <a href="/cadastraProduto">Cadastrar Novo Produto</a>
        '''

@get('/cadastraProduto')
def cadastro_form():
    return '''  <h1>Cadastro de Produto</h1></p>
                <form method="POST" action="/cadastrar">
                Codigo : <input name="codigo"     type="text" /></p>
                Descricao : <input name="descricao"     type="text" /></p>
                Preco : <input name="preco"     type="text" /></p>
                Codigo Fabricante : <input name="codigoFabricante"     type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/cadastrar')
def cadastrar_submit(db):
    codigo     = request.forms.get('codigo')
    descricao     = request.forms.get('descricao')
    preco     = request.forms.get('preco')
    codigoFabricante     = request.forms.get('codigoFabricante')
    try:
        db.execute("INSERT INTO produtos (codigo, descricao, preco, codigoFabricante ) values ('%s', '%s', '%s', '%s')"%(codigo, descricao, preco, codigoFabricante))
        return '''<p>Produto Cadastrado com Sucesso</p>
                    <a href="/consultaProduto">Consultar Produto</a></p>
                    <a href="/cadastraProduto">Cadastrar Novo Produto</a>
                    '''
    except Exception, e:
        return '''<p>Erro ao cadastrar Produto</p>
                     <a href="/cadastraProduto">Voltar</a>
        '''


@get('/deletarProduto')
def deletar_form():
    return '''  <h1>Exclusao de Produto</h1></p>
                <form method="POST" action="/deletar">
                Codigo : <input name="codigo"     type="text" /></p>
                <input type="submit" />
              </form>
                '''

@post('/deletar')
def deletar_submit(db):
    codigo     = request.forms.get('codigo')
    try:
        db.execute('DELETE FROM produtos WHERE codigo = ?', (codigo,))
        return '''<p>Produto Deletado com Sucesso</p>
                    <a href="/consultaProduto">Consultar Produto</a></p>
                    <a href="/cadastraProduto">Cadastrar Novo Produto</a></p>
                    <a href="/deletarProduto">Deletar Produto</a>
                    '''
    except Exception, e:
        return "<p>Erro ao deletar Produto</p>"

@get('/listarProduto')
def listar_produtos(db):
    try:
        c = db.execute('SELECT codigo, descricao, preco, codigoFabricante FROM produtos')
        result = c.fetchall()
        #montar lista de itens
        items = []
        for row in result:
            items.append(Item(row['codigo'],row['descricao'],row['preco'],row['codigoFabricante']))

        table = ItemTable(items)
        return table.__html__()
    except Exception, e:
        return "<p>Erro ao listar Produto</p>"



class ItemTable(Table):
    codigo = Col('Codigo')
    descricao = Col('Descricao')
    preco = Col('Preco')
    codigoFabricante = Col('Codigo do Fabricante')

class Item(object):
    def __init__(self, codigo, descricao, preco, codigoFabricante ):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.codigoFabricante = codigoFabricante



run(reloader=True, host='localhost', port=8003,debug=True)