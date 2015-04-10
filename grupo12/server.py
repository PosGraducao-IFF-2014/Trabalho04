from bottle import get, post, request, run

db = 'usuarios.txt'
dbcomissao = 'comissao.txt'

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

def inserircomissao(comissao):
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

@get('/cadastrarcomissao') # or @route('/registra')
def login_registra():
    return '''  <h1>Cadastrar Comissao</h1></p>
                <form method="POST" action="/registra">
                Codigo da Comissao : <input name="codcomissao"  type="text" /><br/>
                Codigo do Funcionario : <input name="codfuncionario" type="text" /><br/>
                Ano : <input name="ano" type="text" /><br/>
                Mes : <input name="mes" type="text" /><br/>
                Valor : <input name="valor" type="text" /><br/>
                <input type="submit" />
              </form>'''

@post('/cadastrarcomissao') # @route('/registra', method ='post')
def registra():

    pcomissao = request.forms.get('codcomissao')
    pfunc = request.forms.get('codfuncionario')
    pano = request.forms.get('ano')
    pmes = request.forms.get('mes')
    pvalor = request.forms.get('valor')

    comissao ={'pcomissao':pcomissao,'pfunc':pfuncionario, 'pano':pano, 'pmes':pmes, 'pvalor':pvalor  }
    print 'Teste com sucesso'
    if servico.cadastraComissao(comissao):
	   print 'Cadastrado com sucesso'


@get('/telaprincipal') # or @route('/registra')
def login_registra():
    return '''  <h1>Tela Principal</h1></p>
                   <form method="POST" action="/login">
                  </form>
                  <a href="/cadastrarcomissao">Cadastrar Comissao</a><br/><br/>
                  <a href="/registra">Consultar Comissao</a><br/><br/>
                  <a href="/registra">Detelar Comissao</a><br/><br/>
                  <a href="/registra">Calcular Comisssao</a><br/><br/><br/>
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
