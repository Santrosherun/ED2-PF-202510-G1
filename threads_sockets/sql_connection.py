from mysql.connector import connect, errorcode, Error
from os import environ
import pandas as pd

config = {
    "user": environ['DATABASE_USERNAME'],
    "password": environ['DATABASE_PASSWORD'],
    "host": environ['DATABASE_HOST'],
    "database": environ['DATABASE_NAME'],
    "charset": 'utf8'
}


def get_connection():
    """
    The code defines functions to establish a database connection and retrieve data using a specified
    query.
    :return: The `get_connection` function returns a database connection object if the connection is
    successful, or None if there is an error. The `get_data` function returns the result of executing a
    query on the database using the provided connection object.
    """
    try:
        return connect(**config)
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


def get_data(connection: connect, query: str):
    my_cursor = connection.cursor()
    my_cursor.execute(query)
    data = my_cursor.fetchall()
    my_cursor.close()
    return data

