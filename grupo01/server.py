from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
import urllib
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2
import json


@post('/cadastraEstoque')
def cadastraEstoque(db):
	codigo = request.forms.get('codigo')
	localizacao = request.forms.get('localizcao')
	descricao 	= request.forms.get('descricao')
	c = db.execute('INSERT INTO Estoque (codigo, descricao, localizacao) VALUES (codigo,\'descricao\',\'localizacao\')')
		
	print('Cadastrado com suscess')

@route('/delete/<post_id:int>')
def deleteEstoque(db,id):
		try:
	        url = "http://localhost:8004/consulta_estoque/"+str(post_id)
	        request = urllib2.Request(url)

	        # Abre a conexão
	        fd = urllib2.urlopen(request,timeout=2)

	        # Efetua a leitura do conteúdo.
	        content =  fd.readlines()

	        fd.close()
	        print(content)
	        return content

        return content

	    except HTTPError, e:
	        print("Ocorreu um erro ao requisitar o conteúdo do servidor!\n")
	        print("Cod.: ", e.code)

	    except URLError, e:
	        print("URL inválido!\n")
	        print("Mensagem: ", e.reason)

@get('/listaEstoque')
def listaEstoque(db):
	response.content_type = 'application/json'
	c = db.execute('SELECT * FROM Estoque ORDER BY descricao ASC ')
	retornoEstoque = []
	for row in db.execute('SELECT * FROM stocks ORDER BY price'):
		retornoEstoque.append(row)
    return json.dump(retornoEstoque)

run(reloader=True, host='localhost', port=8001,debug=True)