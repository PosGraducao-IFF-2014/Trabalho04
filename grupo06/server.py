from bottle import get, post, request, run

db = 'usuarios.txt'
dbcliente = 'cliente.txt'

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

def inserircliente(cliente):
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

@post('/cadastrarcliente') # @route('/cadastrarcliente', method ='post')
def cadastrarcliente():

    pcod = request.forms.get('codcliente')
    pnome = request.forms.get('nomecliente')
    pcontato = request.forms.get('contato')
    
    conexao = open(dbcliente,'a')
    conexao.write('%s|%s|%s\n' % (pcod,pnome,pcontato))
    conexao.close()
    return 'Cliente cadastrado com sucesso'


@get('/cadastrarcliente') # or @route('/cadastrarcliente')
def login_registracli():
    return '''  <h1>Cadastrar Cliente</h1></p>
                <form method="POST" action="/cadastrarcliente">
                Codigo do Cliente : <input name="codcliente"  type="text" /><br/>
                Nome do Cliente : <input name="nomecliente" type="text" /><br/>
				Contato : <input name="contato" type="text" /><br/>
                <input type="submit" />
              </form>'''


@get('/telaprincipal') # or @route('/registra')
def login_registra():
    return '''  <h1>Tela Principal</h1></p>
                   <form method="POST" action="/login">
                  </form>
                  <a href="/cadastrarcliente">Cadastrar Cliente</a><br/><br/>
                  <a href="/registra">Consultar Cliente</a><br/><br/>
                  <a href="/registra">Detelar Cliente</a><br/><br/>
                  <a href="/login">Sair</a>
                  '''

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
        return ''' <p>Login Correto</p>
                   <a href="/telaprincipal">Entar</a>
                   '''
    else:
        return '''<p>Login Incorreto</p>
                  <a href="/login">Voltar</a>
                  '''



run(reloader=True, debug=True)
