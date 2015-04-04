from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin
from flask_table import Table, Col



install(SQLitePlugin(dbfile='compras.sqlite'))


@route('/existe/<post_id:int>')
def existe(db, post_id):
    response.content_type = 'application/json'
    c = db.execute('SELECT codigoCompra, codigoFornecedor FROM compras WHERE codigoFornecedor = ?', (post_id,))
    row = c.fetchone()
    if row==None:
        return False
    else:
        return True


run(reloader=True, host='localhost', port=8007,debug=True)
