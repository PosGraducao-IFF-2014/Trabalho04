create table venda (
    id integer primary key autoincrement not null,
    codigo_venda text,
    codigo_cliente text,
    codigo_funcionario text,
    data date,
    valor_total text,
    codigo_produto text,
    quantidade text
);