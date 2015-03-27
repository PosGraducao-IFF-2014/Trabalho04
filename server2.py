from bottle import get, post, request, run

db = 'usuarios.txt'

def login(user):
    try:
        linhas = open(db,'r').read()
    except:
        return False

    for linha in linhas.split('\n'):

        if linha == '':
           break
        user1,passwd = linha.split('|')
        if user['usuario'] == user1 and user['senha'] == passwd:
            return True
    return False



@post('/registra') # @route('/registra', method ='post')
def registra():

    usuario     = request.forms.get('name')
    senha = request.forms.get('password')
    user ={'usuario':usuario,'senha':senha}

    if login(user):
       return "<p>Usuario ja cadastrado</p>"
    else:

        conexao = open(db,'a')
        conexao.write('%s|%s\n' % (user['usuario'],user['senha']))
        conexao.close()
        return "<p>Usuario cadastrado</p>"



@get('/registra') # or @route('/registra')
def login_registra():
    return '''  <h1>Registra</h1></p>
                <form method="POST" action="/registra">
                Nome : <input name="name"     type="text" /></p>
                Senha: <input name="password" type="password" />
                <input type="submit" />
              </form>'''




@get('/login') # or @route('/login')
def login_form():
    return '''  <h1>Login</h1></p>
                <form method="POST" action="/login">
                Nome : <input name="name"     type="text" /></p>
                Senha: <input name="password" type="password" />
                <input type="submit" />
              </form>
              <a href="/registra">Registra</a>
                '''

@post('/login') # or @route('/login', method='POST')
def login_submit():
    usuario     = request.forms.get('name')
    senha = request.forms.get('password')
    user ={'usuario':usuario,'senha':senha}
    if login(user):
        return "<p>Your login was correct</p>"
    else:
        return "<p>Login failed</p>"



run(reloader=True, debug=True)
