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
    else : 
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

    with open ('data.csv','r') as f : 
        variables = csv.reader(f)
        next(variables)

        for variable in variables:
            country_name = variable[0]
            region_name = variable[2]
            city_name = variable[1]
            population = variable[3]
            country_id = insert_country(country_name)
            region_id = insert_region(country_id, region_name, country_name)
            city_id = insert_city(region_id, city_name, population, region_name)



try:
    cur = conn.cursor()
except (Exception) as error:
    print(error)


cur.execute("""select * from country as c
join region as r on c.id = r.country_id
join city as ci on ci.region_id = r.id
order by population desc""" )

info = cur.fetchall()
print(info[0])

