create table produto_estoque (
    id              integer primary key autoincrement not null,
    codigo_estoque  integer,
    codigo_produto  integer,
    quantidade      integer
);

