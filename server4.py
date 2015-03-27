# -*- coding: utf-8 -*-
from bottle import post,get, install, HTTPError, run
import urllib
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2

@get('/volta/<post_id:int>')
def volta(post_id):

    try:
        url = "http://localhost:8080/teste/"+str(post_id)
        request = urllib2.Request(url)

        # Abre a conexão
        fd = urllib2.urlopen(request,timeout=2)

        # Efetua a leitura do conteúdo.
        content =  fd.readlines()

        fd.close()
        print(content)
        return content

#        return content

    except HTTPError, e:
        print("Ocorreu um erro ao requisitar o conteúdo do servidor!\n")
        print("Cod.: ", e.code)

    except URLError, e:
        print("URL inválido!\n")
        print("Mensagem: ", e.reason)

run(reloader=True, host='localhost', port=8081,debug=True)
