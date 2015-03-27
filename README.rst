Trabalho 04

	WebService da Pos-Graduação -2014-2

	Implementação de Sistemas de Vendas

	Os grupos deverão implementar clientes e servidor para os métodos descritos

	Os grupos deverão refazer os métodos descritos utilizando restful(bootle) e banco de dados(sqlite)

	Use o numero do Grupo como Complemento da porat TCP no server
	Ex:Grupo 01 => porta : 8001

	Os membros do Grupo deverão pegar a tarefa na Issue Correspondente


Grupo 01
	cadastraEstoque(Estoque)

		Estoque = {codigo,descricao,localizao}

		DeleteEstoque (codigoEstoque)

	verificar se exite algum produto cadastrado ProdutoEstoque

		listaEstoque( )

		consultaEstoque(codigoEstoque)

Grupo 02
	cadastraFabricante(Fabricante)

		Fabricante = {codigo,descricao,localizao}

		DeleteFabricante (codigoFabricante)

	verificar se exite algum fabricante cadastrado em Produto

		listaFabricante( )
		consultaFabricante(codigoFabricante)


Grupo 03
	cadastrarProduto(Produto)

		Produto = {codigo,descricao,preco, codigoFabricante}

		deletarProduto(codigoproduto)

	Verificar se produto esta em algum estoque

		listarProduto()

		consultaProduto(codigoProduto)

Grupo 04
	inserirProdutoEstoque(CodigoEstoque,codigoProduto,quantidade)

	verificar se o estoque e produto existem

		consultaProdutoEmEstoque(codigoProduto)

		consultaEstoqueemProdutoEstoque(codigoEstoque)

		pesquisaPreçoProdutoEstoque(codigoproduto,codigoestoque)

Grupo 05
	cadastraFornecedor(Fornecedor)

		Fornecedor = {codigo,nome,contato}

		deletarFornecedor(codigoFornecedor)

	Verificar se fornecedor esta em algum compra

		listarFornecedor()

		consultaFornecedor(codigoFornecedor)

Grupo 06
	cadastraCliente(Cliente)

		Cliente = {codigo,nome,contato}

		deletarCliente (codigoCliente )

	Verificar se Cliente esta em algum venda

		consultarCliente(codigoCliente)


Grupo 07
	cadastrarCompra(Compra)

		Compra={codigoCompra ,{codigoProduto,quantidade},data,valortotal,codigoFornecedor}

		consultarCompra (codigoCompra )

		deletarCompra (codigoCompra )

Grupo 08
	cadastrarFuncionario(Funcionario)

		Funcionario = {codigoFuncionario,nome,endereco,sexo,datanascimento}

		consultatFuncionario(codigoFuncionario)

		deletarFuncionario(codigo)

			verificar se não existe venda

Grupo 09

	cadastrarVenda(Venda)

		Venda = {codigoVenda,codigoCliente,codigoFuncionario,data,valortotal,{codigoProduto,quantidade}}

		consultarVenda(codigoVenda)

		deletarVenda(codigoVenda)

Grupo 10
	cadastrarContaApagar(ContaApagar)

		ContaApagar = {codigoApagar, codigoCompra, dataVencimento, dataPagamento, status}

		consultarAPagar(codigoApagar)

		deletarApagar(codigoApagar)

Grupo 11
	cadastrarContaAreceber(ContasAreceber)

		ContasArecebe = {codigoAreceber, codigoVenda,dataVencimento,dataPagamento, status}

		consultarAreceber(codigoAreceber)

		deletarAreceber(codigoAreceber)

Grupo 12
	calcularComissao(Comissão)

		Comissão = {codigoComissao,codigoFuncionario,ano,mes,valor}

		consultarComissaoFuncionario( codigoFuncionario,ano,mes)

		deletaComissaoFuncionario(codigoFuncionario,ano,mes)





Utilizando o Allserver.py


	Inicializar todos os server's

		python allservers.py start

	Matar todos os server's

		python allservers.py kill

	Restart os server´s

		python allservers.py restart


Atualização do Git no Ubuntu(caso necessario)

	Passo 01

	   sudo apt-get remove git-core

	Passo 02
	   sudo add-apt-repository ppa:git-core/candidate

	Passo 03
	    sudo apt-get update && apt-get upgrade

	Passo 04

	    sudo apt-get install git-core

