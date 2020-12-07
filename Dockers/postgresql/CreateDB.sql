CREATE TABLE clientes (
    client_id serial PRIMARY KEY,
    client_name varchar(255) NOT NULL,
    years numeric(3,0) NOT NULL,
    email varchar(255) NOT NULL,
    idioma varchar(255) NOT NULL,
    enviromental_score numeric(1,0) NOT NULL,
    transport varchar(50) NOT NULL,
    work_preference varchar(50) NOT NULL,
    place_score numeric(1,0) NOT NULL,
    season varchar(50) NOT NULL,
    size_preference varchar(50) NOT NULL,
    entreteiment boolean NOT NULL,
    salary numeric(10,3) NOT NULL,
    percentaje_home numeric(3,0) NOT NULL,
    interest_variable varchar(50) NOT NULL
);

CREATE TABLE datos (
    city_id serial PRIMARY KEY,
    city_name varchar(255) UNIQUE ,
    languages varchar(50) ,
    pollution double precision ,
    best_mobility_option varchar(255) ,
    work_spaces integer ,
    mountain boolean ,
    beach boolean ,
    c_temp double precision,
    c_rainy_days integer,
    c_population double precision,
    density double precision,
    leisure double precision,
    housing double precision,
    cpi double precision,
    gdp_pc double precision,
    tax_burden double precision,
    crime_rate double precision,
    hdi double precision,
    doing_business integer,
    freedom double precision,
    life_expectancy double precision
);