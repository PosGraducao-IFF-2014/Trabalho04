from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='db.sqlite'))

@get('/consulta_venda/<codigo_venda>')
def consulta_venda(db, codigo_venda):
    total = db.execute("""
    select count(*) as total from venda
    where codigo_venda = %s""" % (codigo_venda,)).fetchone()['total']
    return '1' if total > 0 else '0'