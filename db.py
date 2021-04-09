import sqlite3

conn = sqlite3.connect("users.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE user (
    id integer PRIMARY KEY,
    name text NOT NULL,
    age integer NOT NULL,
    mobile text NOT NULL
)"""
cursor.execute(sql_query)