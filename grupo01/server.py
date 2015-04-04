from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
import urllib
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2


@post('/cadastraEstoque')
def cadastraEstoque(db):
	codigo = request.forms.get('codigo')
	localizacao = request.forms.get('localizcao')
	descricao 	= request.forms.get('descricao')
	#c = db.execute('INSERT INTO Estoque (codigo, descricao, localizacao) VALUES (codigo,\'descricao\',\'localizacao\')')
	db.execute("INSERT INTO Estoque (codigo, descricao, localizacao) values ('%s' ,'%s', '%s')"%(codigo,localizacao, descricao))
	print('Cadastrado com suscess')

@route('/delete/<post_id:int>'
def deleteEstoque(db,id):
		try:
	        url = "http://localhost:8004/teste/"+str(post_id)
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

run(reloader=True, host='localhost', port=8001,debug=True)