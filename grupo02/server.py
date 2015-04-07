from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
import urllib
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2
import json

install(SQLitePlugin(db='fabricante.db'))

@post('/cadastraFabricante')
def cadastraFabricante(db):
	codigo = request.forms.get('codigo')
	localizacao = request.forms.get('localizacao')
	descricao 	= request.forms.get('descricao')
	c = db.execute('INSERT INTO fabricante (codigo, descricao, localizacao) VALUES (codigo,\'descricao\',\'localizacao\')')
		
	print('Sucesso!')

@route('/DeleteFabricante /<id:int>')
def DeleteFabricante (db, id):

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

        return True

    except HTTPError, e:
        print("Ocorreu um erro ao acessar o servidor!\n")
        print("Cod.: ", e.code)
        return False
    except URLError, e:
        print("URL inválida!\n")
        print("Mensagem: ", e.reason)
        return False

@get('/listaFabricante')
def listaFabricante(db):
    response.content_type = 'application/json'
    response_ = []
    for row in db.execute('SELECT * FROM Fabricante ORDER BY nome ASC'):
        response_.append(row)

    return json.dump(response_)

run(reloader=True, host='localhost', port=8002, debug=True)
