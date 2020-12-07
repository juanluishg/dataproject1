CREATE TABLE clientes (
    client_id serial PRIMARY KEY,
    client_name varchar(255) ,
    years numeric(3,0) ,
    email varchar(255) ,
    idioma varchar(255) ,
    enviromental_score numeric(1,0) ,
    transport varchar(50) ,
    work_preference varchar(50) ,
    place_score numeric(1,0) ,
    season varchar(50) ,
    size_preference varchar(50) ,
    entreteiment boolean ,
    salary numeric(10,3) ,
    percentaje_home numeric(3,0) ,
    interest_variable varchar(50)
);

CREATE TABLE weather (
    id integer PRIMARY KEY,
    w_month integer,
    w_year integer,
    c_temp double precision,
    c_rainy_days integer
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
    c_weather integer REFERENCES weather(id),
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

