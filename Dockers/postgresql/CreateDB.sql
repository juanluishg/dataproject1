CREATE TABLE clientes (
    client_id serial,
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
    interest_variable varchar(50),
    PRIMARY KEY(client_id)
);

CREATE TABLE datos (
    city_id serial,
    city_name varchar(255) UNIQUE ,
    languages varchar(50) ,
    pollution double precision ,
    best_mobility_option varchar(255) ,
    work_spaces integer ,
    mountain boolean ,
    beach boolean ,
    c_temp double precision,
    c_rainy_days integer,
    c_weather integer,
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
    life_expectancy double precision,
    PRIMARY KEY(city_id),
    CONSTRAINT fk_datos
        FOREIGN KEY(c_weather)
            REFERENCES weather(id)
);

CREATE TABLE weather (
    id integer PRIMARY KEY,
    city_id integer,
    month integer
    year integer
    c_temp double precision,
    c_rainy_days integer,
    CONSTRAINT fk_weather
        FOREIGN KEY(city_id)
            REFERENCES datos(city_id)
    )