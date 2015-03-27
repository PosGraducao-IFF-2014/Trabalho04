# -*- coding: utf-8 -*-
from bottle import route, install, template, run, get, post, response, request
from bottle_sqlite import SQLitePlugin



install(SQLitePlugin(dbfile='usuario.sqlite'))

@route('/show/<post_id:int>')
def show(db, post_id):
    c = db.execute('SELECT usuario, password FROM usuarios WHERE id = ?', (post_id,))

    row = c.fetchone()

    return template('show_post', usuario=row['usuario'], password=row['password'])


@get('/teste/<post_id:int>')
def redit(db,post_id):

    response.content_type = 'application/json'

    c = db.execute('SELECT usuario, password FROM usuarios WHERE id = ?', (post_id,))

    row = c.fetchone()
    return {'usuario':row['usuario'], 'password':row['password']}


@get('/login')
def login_form():
    return '''  <h1><center>Login</center></h1></p>
                    <form method="POST" action="/login">

                        <table align="center">
                            <tr>
                                <td>Usuario:</td>
                                <td><input name="usuario" type="text" size="10" /></td>
                            </tr>
                            <tr>
                                <td>Senha:</td>
                                <td><input name="password" type="text" size="3" /></td>
                            </tr>

                            </table>
                            <br>
                            <center><input type="submit" value="Salvar" /></center>
                    </form>
                <center><a href="/">Voltar</a></center>
            '''

#------------------------------------------------------------------------------------------------------------

#Cadastro de Produto
@post('/login')
def login(db):
    usuario = request.forms.get('usuario')
    password = request.forms.get('password')
    db.execute("INSERT INTO usuarios (usuario, password) values ('%s', '%s')"%(usuario, password))

#-----------------------------------------

run(reloader=True, debug=True)
