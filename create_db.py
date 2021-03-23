import psycopg2
import sys


# This .py connects to the localhost postgresql and creates a new database "beers_reviews_db".
# Set your own db configs on main function.

def connect_db(params_dic):
    conn = None
    try:
        # connect to the PostgreSQL server
        print('%s database...' % params_dic.get("database"), end='')
        conn = psycopg2.connect(**params_dic)
        conn.autocommit = True
    except Exception as error:
        print("Unable to connect: ", error)
        sys.exit(1)
    print("Connection successful!")
    return conn, conn.cursor()


def execute_sql(conn, cursor, sql_list):
    try:
        for sql in sql_list:
            cursor.execute(sql)
    except Exception as error:
        print(error)
    finally:
        conn.close()
        cursor.close()


def main():

    # Set your local variables here!
    params = dict(
        database="postgres",
        user="postgres",
        host="127.0.0.1",
        port="5432",
        password="new_password")

    sql_breweries = """create table breweries (
        id INTEGER not null,
        name VARCHAR(250) NOT NULL,
        city VARCHAR(50),
        state VARCHAR(10),
        country VARCHAR(10),
        notes VARCHAR(2000),
        types VARCHAR(60),
        CONSTRAINT breweries_pk PRIMARY KEY (id)
    )"""

    sql_beers = """create table beers (
        id INTEGER not null,
        name VARCHAR(250) NOT NULL,
        brewery_id  INTEGER NOT NULL,
        state VARCHAR(10),
        country VARCHAR(10),
        style VARCHAR(50),
        availability VARCHAR(50),
        abv NUMERIC(5,2),
        notes VARCHAR(5000),
        retired VARCHAR(20),
        CONSTRAINT beers_pk PRIMARY KEY (id),
        CONSTRAINT brewery_fk FOREIGN KEY (brewery_id) references breweries (id)
    )"""

    sql_reviews = """create table reviews (
        beer_id INTEGER NOT NULL,
        username VARCHAR(50) NOT NULL,
        "date" DATE not null,
        text VARCHAR(5000),
        look numeric(4, 2),
        smell numeric(4, 2),
        taste numeric(4, 2),
        feel numeric(4, 2),
        overall numeric(4, 2),
        score numeric(4, 2),
        CONSTRAINT reviews_pk PRIMARY KEY (beer_id, username, "date"),
        CONSTRAINT beers_fk FOREIGN KEY (beer_id) references beers (id)
    )"""

    # Connect to postgresql
    conn, cursor = connect_db(params)

    sql_list = list()

    # Create database beers_reviews_db
    sql_list.append("DROP DATABASE IF EXISTS beers_reviews_db")
    sql_list.append("CREATE database beers_reviews_db")
    execute_sql(conn, cursor, sql_list)
    print("Database beers_reviews_db created successfully!")

    # Connect to database beers_reviews_db
    params.update(database="beers_reviews_db")
    conn, cursor = connect_db(params)

    # Create tables
    sql_list.clear()
    sql_list.append("DROP TABLE IF EXISTS breweries CASCADE")
    sql_list.append("DROP TABLE IF EXISTS beers CASCADE")
    sql_list.append("DROP TABLE IF EXISTS reviews CASCADE")
    sql_list.append("DROP TABLE IF EXISTS max_rated CASCADE")
    sql_list.append(sql_breweries)
    sql_list.append(sql_beers)
    sql_list.append(sql_reviews)
    execute_sql(conn, cursor, sql_list)
    print("Tables created successfully!")


if __name__ == "__main__":
    main()
