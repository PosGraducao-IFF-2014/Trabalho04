# -*- coding: utf-8 -*-
from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin

#CREATE TABLE "ContasApagar" ("codigoApagar" INTEGER PRIMARY KEY  NOT NULL  UNIQUE , "codigoCompra" INTEGER, "dataVencimento" DATETIME, "dataPagamento" DATETIME, "status" VARCHAR)

install(SQLitePlugin(dbfile='contas.sqlite'))

@route('/show/<codigoApagar:int>')
def show(db, codigoApagar):
    c = db.execute('SELECT codigoCompra, dataVencimento, dataPagamento, status FROM ContasApagar WHERE codigoApagar = ?', (codigoApagar,))

    row = c.fetchone()

    return template('show_post', compra=row['codigoCompra'], vencimento=row['dataVencimento'], pagamento=row['dataPagamento'], status=row['status'])


@get('/teste/<codigoApagar:int>')
def redit(db,codigoApagar):

    response.content_type = 'application/json'

    c = db.execute('SELECT codigoCompra, dataVencimento, dataPagamento, status FROM ContasApagar WHERE codigoApagar = ?', (codigoApagar,))

    row = c.fetchone()
    return {'Compra':row['codigoCompra'],'Vencimento':row['dataVencimento'], 'Pagamento':row['dataPagamento'], 'Status':row['status']}


@get('/consulta')
def consulta_form():
    return '''  <h1><center>Consulta</center></h1></p>
                    <form method="POST" action="/consulta">

                        <table align="center">
                            <tr>
                                <td>Compra:</td>
                                <td><input name="codigoCompra" type="text" size="10" /></td>
                            </tr>
			    <tr>
                                <td>Vencimento:</td>
                                <td><input name="dataVencimento" type="text" size="10" /></td>
                            </tr>
			    <tr>
                                <td>Pagamento:</td>
                                <td><input name="dataPagamento" type="text" size="10" /></td>
                            </tr>
                            <tr>
                                <td>Status:</td>
                                <td><input name="status" type="text" size="10" /></td>
                            </tr>

                            </table>
                            <br>
                            <center><input type="submit" value="Salvar" /></center>
                    </form>
                <center><a href="/">Voltar</a></center>
            '''

#------------------------------------------------------------------------------------------------------------

#Cadastro de Produto
@post('/consulta')
def consulta(db):
    compra = request.forms.get('codigoCompra')
    vencimento = request.forms.get('dataVencimento')
    pagamento = request.forms.get('dataPagamento')
    status = request.forms.get('status')
    db.execute("INSERT INTO ContasApagar (codigoCompra, dataVencimento, dataPagamento, status) values ('%s', '%s', '%s', '%s')"%(compra, vencimento, pagamento, status))

#-----------------------------------------

run(reloader=True, debug=True)
