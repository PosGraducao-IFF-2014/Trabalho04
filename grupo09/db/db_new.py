# -*- coding: utf-8 -*-
import os
import sqlite3

db_filename = 'venda.sqlite'
schema_filename = 'schema.sql'
db_is_new = not os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
      with open(schema_filename, 'rt') as f:
        schema = f.read()
      conn.executescript(schema)
      conn.execute("""
      insert into venda(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade)
      values (1, 1, 1, 200112, 25.00, 5, 4)
      """)
      conn.execute("""
      insert into venda(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade)
      values (1, 1, 1, 20/01/12, 25.00, 5, 4)
      """)
      conn.execute("""
      insert into venda(codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade)
      values (1, 1, 1, 20/01/12, 25.00, 5, 4)
      """)
    else:
      print "Database exists"