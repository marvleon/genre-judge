# Marvin Leon cs430
# This file contains the derived data model class that supports creation and reading of entries
# via a sqlite3 database. This is the backend code.

# The abstract base class Model is imported along with the sqlite3 package.
# The file storing the database (quotes.db) will be created in the directory that the web
# app is run from and will persist across invocations. 

# The model constructor creates a connection to the file and attempts a query to see
# if the "quotes" table exists in the file. If not, then it will create the table and schema.

from .Model import Model
import sqlite3

DB_FILE = 'quotes.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from quotes")
        except sqlite3.OperationalError:
            cursor.execute("create table quotes (quote text, author text, source text, date text)")
        cursor.close()

    def select(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quotes")
        return cursor.fetchall()

    def insert(self, quote, author, source, date):
        params = {'quote': quote, 'author': author, 'source': source, 'date': date}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into quotes (quote, author, source, date) VALUES (:quote, :author, :source, :date)", params)
        connection.commit()
        cursor.close()
        return True
