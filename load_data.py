import pandas as pd
import psycopg2
import psycopg2.extras as extras
import sys


# Set your own db variables on main function.

# DB connection
def connect_db(params_dic):

    try:
        # Connect to the PostgreSQL server
        print('%s database...' % params_dic.get("database"), end='')
        conn = psycopg2.connect(**params_dic)
        conn.autocommit = True
    except Exception as error:
        print("Unable to connect: ", error)
        sys.exit(1)
    else:
        print("Connection successful!")
        return conn.cursor()


# Inserts data into db by a given DataFrame.
def execute_insert(cursor, df, table):

    # Creates tuples
    tpls = [tuple(x) for x in df.to_numpy()]

    # Identifies columns
    cols = ','.join(list(df.columns))

    # Creates sql
    sql = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)

    try:
        extras.execute_values(cursor, sql, tpls)
        print("Data was successfully inserted into %s." % table)
    except Exception as err:
        print(err)


def load_df(csv_file_path):

    return pd.read_csv(csv_file_path, encoding='utf-8')


def main():
    # Set your connection variables here
    params = dict(
        database="beers_reviews_db",
        user="postgres",
        host="127.0.0.1",
        port="5432",
        password="new_password")

    # Set you .csv paths here
    csv_breweries = "files/breweries.csv"
    csv_beers = "files/beers.csv"
    csv_reviews = "files/reviews.csv"

    try:
        cursor = connect_db(params)
        execute_insert(cursor, load_df(csv_breweries), "breweries")
        execute_insert(cursor, load_df(csv_beers), "beers")
        execute_insert(cursor, load_df(csv_reviews), "reviews")
    except Exception as err:
        print(err)
    else:
        cursor.close()


if __name__ == "__main__":
    main()
