<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Grupo 04</title>
    <style type="text/css">
      table, td, th
      {
        border: 3px solid black;
        font-size: large;
        font-weight: 300;
      }
      .erro {
        background-color: red;
      }
    </style>
  </head>
  <body>
  <center>
    <h1>Gerenciar produto em estoque:</h1>
    <table>
      <tr>
        <th>Código</th>
        <th>Codigo Estoque</th>
        <th>Codigo Produto</th>
        <th>Quantidade</th>
      </tr>
      %for produto_estoque in produtos_estoques:
      <tr>
        <td> <center> {{ produto_estoque['id'] }} </center> </td>
        <td> <center> {{ produto_estoque['codigo_estoque'] }} </center> </td>
        <td> <center> {{ produto_estoque['codigo_produto'] }} </center> </td>
        <td> <center> {{ produto_estoque['quantidade'] }} </center> </td>
      </tr>
      %end
    </table>
  %if erro:
    <p class='erro'>{{ erro }}</p>
  %end
	<p>
	<form action="/produto_estoque" method="post">
	<label for="codigo_produto">Informe codigo do produto:</label>
	<input type="number" name="codigo_produto" /> </p>
	<p>
	<label for="codigo_estoque">Informe codigo do estoque:</label>
	<input type="number" name="codigo_estoque" /> </p>
	<p>
	<label for="quantidade">Informe quantidade:</label>
	<input type="number" name="quantidade" /> </p>

	<input type="submit" value="Enviar" />
	</form>

  </center>
  </body>
</html>
