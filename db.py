from email import header
from tabnanny import check
import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="weather_application",
    user="postgres",
    password="1")
cur = conn.cursor()


def create_table():
    sql_query = '''
    CREATE TABLE if not exists  "country" (
    "id" serial,
    "name" varchar(50),
    PRIMARY KEY ("id")
    );

    CREATE TABLE if not exists "region" (
    "id" serial,
    "country_id" int,
    "name" varchar(50),
    PRIMARY KEY ("id"),
    FOREIGN KEY ("country_id") REFERENCES "country"("id")
    );

    CREATE TABLE if not exists  "city" (
    "id" serial,
    "region_id" int,
    "name" varchar(50),
    "population" int,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("region_id") REFERENCES "region"("id")
    );'''
    cur.execute(sql_query)
    conn.commit()
    insert_alldata()


def insert_country(country_name):
    cur.execute(f"""select id from country where name = '{country_name}'""")
    check_country = cur.fetchone()
    if check_country is None:
        cur.execute(
            f"""insert into country (name) values ('{country_name}') returning id;""")
        conn.commit()
        country_id = cur.fetchone()[0]
        return (country_id)
    else:
        return check_country[0]


def insert_region(country_id, region_name, country_name):
    cur.execute(f"""select id from region where name = '{region_name}'""")
    check_region = cur.fetchone()
    if check_region is None:
        cur.execute(
            f"""insert into region (country_id,name) values ({country_id},'{region_name}') returning id;""")
        conn.commit()
        region_id = cur.fetchone()[0]
        return (region_id)
    else:
        return check_region[0]


def insert_city(region_id, city_name, population, region_name):
    cur.execute(f"""select id from city where name = '{city_name}'""")
    check_region = cur.fetchone()

    if check_region is None:
        cur.execute(
            f"""insert into city (region_id,name,population) values ({region_id},'{city_name}',{population}) returning id;""")
        conn.commit()
        city_id = cur.fetchone()[0]
        return (city_id)
    elif check_region is not None:
        cur.execute(f"""select id from city where name = '{city_name}'""")
        conn.commit()
        city_id = cur.fetchone()[0]
        return (city_id)


def insert_alldata():

    with open('data.csv', 'r') as f:
        variables = csv.reader(f)
        next(variables)

        for variable in variables:
            country_name = variable[0]
            region_name = variable[2]
            city_name = variable[1]
            population = variable[3]
            country_id = insert_country(country_name)
            region_id = insert_region(country_id, region_name, country_name)
            city_id = insert_city(region_id, city_name,
                                  population, region_name)


def get_tables(country_name):
    cur.execute(f"""select ci.name,r.name,ci.population from country as c 
join region as r on c.id = r.country_id
join city as ci on r.id = ci.region_id
where c.name = '{country_name}'
order by population desc """)
    info = cur.fetchall()
    return info


def get_city_information(city_name):
    cur.execute(f"""select ci.name,r.name,ci.population from country as c 
join region as r on c.id = r.country_id
join city as ci on r.id = ci.region_id
where ci.name = '{city_name}'
""")
    info = cur.fetchall()
    return info


create_table()

try:
    cur = conn.cursor()
except (Exception) as error:
    print(error)
