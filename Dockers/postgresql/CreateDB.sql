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
    pollution numeric(3,3) ,
    best_mobility_option numeric(3,3) ,
    work_spaces numeric(4,0) ,
    mountain boolean ,
    beach boolean ,
    c_temp numeric(3,3),
    c_rainy_days numeric(2,0),
    c_population numeric(10,0),
    density numeric(10,3),
    leisure numeric(10,5),
    housing numeric(3,3),
    cpi numeric(3,3),
    gdp_pc numeric(3,3),
    tax_burden numeric(3,2),
    crime_rate numeric(3,3),
    hdi numeric(3,3),
    doing_business numeric(3,3),
    freedom numeric(3,3),
    life_expectancy numeric(3,2)
);