# -*- coding: utf-8 -*-

import os
import sqlite3

db_filename = 'db.sqlite'
schema_filename = 'schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        conn.execute("""
        insert into produto_estoque(codigo_estoque, codigo_produto, quantidade)
        values (1, 10, 20)
        """)
        conn.execute("""
        insert into produto_estoque(codigo_estoque, codigo_produto, quantidade)
        values (1, 12, 16)
        """)
        conn.execute("""
        insert into produto_estoque(codigo_estoque, codigo_produto, quantidade)
        values (2, 10, 35)
        """)

    else:
        print 'DB já existe!'
