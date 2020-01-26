"""
Creates a "messier_catalog" database with an "Object" table. 
The table is filled with data from messier_catalog.csv file.
"""

import sqlite3
import pandas as pd

# Reading data file
catalog = pd.read_csv("data/messier_catalog.csv", sep=';')
catalog.fillna("", inplace=True)


# Database connection (creates a file if none)
conn = sqlite3.connect('messier_catalog.db')
c = conn.cursor()

# "objects" table creation
c.execute('''CREATE TABLE objects
             (messier_id text, ngc_id text, type text, season text, magnitude integer,
              constellation_en text, constellation_fr text, constellation_latin text,
               ra text, dec text, distance integer, size text, discoverer text,
                year integer, image text, constellation_id text)''')

# Data rows insertion
for row in catalog.itertuples(index=False) :
    query = "INSERT INTO objects VALUES ("
    for i in range(16):
        if row[i] == '':
            query += '" ",'
        else :
            if i in [4, 10, 13]:
                query += str(row[i]) + ","
            else :
                query += '"' + row[i] + '",'
    query = query[:-1] + ')'
    c.execute(query)

# Saving changes
conn.commit()

# Closing connection

conn.close()