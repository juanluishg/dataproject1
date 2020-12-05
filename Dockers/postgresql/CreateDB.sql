CREATE TABLE clientes (
    client_id serial PRIMARY KEY,
    client_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    idioma varchar(255) NOT NULL,
    enviromental_score numeric(1,0) NOT NULL,
    transport varchar()
);

CREATE TABLE datos (
    city_id serial PRIMARY KEY,
    city_name varchar(255) UNIQUE NOT NULL,

);