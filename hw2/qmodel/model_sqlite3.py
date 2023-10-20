# Marvin Leon cs430
# This file contains the derived data model class that supports creation and reading of entries
# via a sqlite3 database. This is the backend code.

# The abstract base class Model is imported along with the sqlite3 package.
# The file storing the database (entries.db) will be created in the directory that the web
# app is run from and will persist across invocations. 

# The model constructor creates a connection to the file and attempts a query to see
# if the "quotes" table exists in the file. If not, then it will create the table and schema.
