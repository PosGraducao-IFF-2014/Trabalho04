# -*- coding: utf-8 -*-
import os
import sqlite3

db_filename = 'funcionario.sqlite'
schema_filename = 'schema.sql'
db_is_new = not os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
      with open(schema_filename, 'rt') as f:
        schema = f.read()
      conn.executescript(schema)
      conn.execute("""
      insert into funcionario(codigo_funcionario,nome_funcionario,endereco_funcionario,sexo_funcionario,datanascimento_funcionario)
      values (001, Luciana, Rua d, feminino,28041990)
      """)
      conn.execute("""
      insert into funcionario(codigo_funcionario,nome_funcionario,endereco_funcionario,sexo_funcionario,datanascimento_funcionario)
      values (002, Talyta, Rua c, Feminino,29011990)
      """)
      conn.execute("""
      insert into funcionario(codigo_funcionario,nome_funcionario,endereco_funcionario,sexo_funcionario,datanascimento_funcionario)
      values (003, carlos, Rua B, Masculino, 04031990)
      """)
    else:
      print "Database exists"