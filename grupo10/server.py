# -*- coding: utf-8 -*-
from bottle import route, install, template, run, get, post, delete, response, request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='contas.sqlite'))

# Grupo 10
# cadastrarContaApagar(ContaApagar)
#      ContaApagar = {codigoApagar, codigoCompra, dataVencimento, dataPagamento, status}
# consultarAPagar(codigoApagar)
# deletarApagar(codigoApagar)

#CREATE TABLE "ContasApagar" ("codigoApagar" INTEGER PRIMARY KEY  NOT NULL  UNIQUE , "codigoCompra" INTEGER, "dataVencimento" DATETIME, "dataPagamento" DATETIME, "status" VARCHAR)

@get('/consultarAPagar/<codigoApagar_id:int>')
def consultarAPagar(db,codigoApagar_id):
	response.content_type = 'application/json'
	
	c = db.execute('SELECT * FROM ContasApagar WHERE codigoApagar = ?', (codigoApagar_id,))
	
	row = c.fetchone()
	
	return {'codigoApagar':row['codigoApagar'], 'codigoCompra':row['codigoCompra'], 'dataVencimento':row['dataVencimento'], 'dataPagamento':row['dataPagamento'], 'status':row['status']}

@delete('/deletarApagar/<codigoApagar_id:int>')
def deletarApagar(db,codigoApagar_id):
	response.content_type = 'application/json'

	db.execute('DELETE FROM ContasApagar WHERE codigoApagar = ?', (codigoApagar_id,))
	
	return {'result':'OK'}

@post('/cadastrarContaApagar')
def cadastrarContaApagar(db):
	response.content_type = 'application/json'

	codigoApagar = request.forms.get('codigoApagar')
	codigoCompra = request.forms.get('codigoCompra')	
	dataVencimento = request.forms.get('dataVencimento')	
	dataPagamento = request.forms.get('dataPagamento')
	status = request.forms.get('status')
	
	db.execute("INSERT INTO ContasApagar (codigoApagar, codigoCompra, dataVencimento, dataPagamento, status) values ('%s', '%s', '%s', '%s', '%s')"%(codigoApagar, codigoCompra, dataVencimento, dataPagamento, status))
	
	return {'result':'OK'}

run(host='localhost', port=8010, debug=True)
