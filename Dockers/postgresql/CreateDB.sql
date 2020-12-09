CREATE TABLE clientes (
    client_id serial PRIMARY KEY,
    client_name varchar(255) ,
    years integer ,
    email varchar(255) ,
    idioma varchar(255) ,
    enviromental_score integer ,
    transport varchar(50) ,
    work_preference varchar(50) ,
    place_score varchar(50) ,
    season varchar(50) ,
    size_preference varchar(50) ,
    entreteiment boolean ,
    salary integer ,
    percentaje_home double precision ,
    interest_variable varchar(50)
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

CREATE TABLE weather (
    id integer PRIMARY KEY,
    city_id integer REFERENCES datos(city_id),
    w_month integer,
    w_year integer,
    c_temp double precision,
    c_rainy_days integer
);