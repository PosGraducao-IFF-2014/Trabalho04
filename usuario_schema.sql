-- Schema for to-do application examples.

-- Projects are high-level activities made up of tasks
create table usuarios (
    id          integer primary key autoincrement not null,
    usuario     text,
    password    text
);

