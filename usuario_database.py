import os
import sqlite3

db_filename = 'usuario.sqlite'
schema_filename = 'usuario_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserting initial data'

        conn.execute("""
        insert into usuarios (usuario, password)
        values ('luiz', '123456')
        """)

        conn.execute("""
        insert into usuarios (usuario, password)
        values ('gustavo', '123456')
        """)

        conn.execute("""
        insert into usuarios (usuario, password)
        values ('dani', '123456')
        """)

    else:
        print 'Database exists, assume schema does, too.'