"""
Database access module
Usage :

get_all_objects()
get_objects(['ngc_id', 'constellation_latin'], {'season':'Autumn', 'type':'Galaxy'})
"""

import sqlite3
import json
import os.path

COLUMNS = ["messier_id", "ngc_id", "type", "season", "magnitude", "constellation_en", "constellation_fr", 
"constellation_latin", "ra", "dec", "distance", "size", "discoverer", "year", "image", "constellation_id"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "messier_catalog.db")

def get_all_objects():
    """
    Queries database to get all rows. 
    Returns a dict of all objects as {messier_id : {object}}

    Returns :
    dict(dict) : all objects
    """
    
    # Database connection 
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Select all object query
    c.execute("SELECT * FROM objects")
    rows = c.fetchall()

    # Closing connection
    conn.close()

    # Found objects to dict {id : {obj}}
    objects = {k[0]:{} for k in rows}
    for row in rows:
        obj = {col:"" for col in COLUMNS[1:]}
        for i in range(1, len(row)):
            obj[COLUMNS[i]] = row[i]
        objects[row[0]] = obj
    return json.dumps(objects)

def get_objects(columns, filter):
    """
    Queries database to return specific rows. 
    Returns a dict of the n found objects as {i : {object}} i->[0:n]

    Parameters :
    columns (list) : data to return by column name
    filter (dict) : dict of filters {"id" : 1, "size" : 4}

    Returns :
    dict : found objects as {0 : {object}, 1 : {object}}
    """

    # Database connection
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Creating queries
    column_query = ",".join(col for col in columns)
    filter_query = ' and '.join(k + "='" + v +"'" for k,v in filter.items())
    
    # Querying database
    c.execute("SELECT " + column_query + " FROM objects where " + filter_query)
    rows = c.fetchall()

    # Close connection
    conn.close()

    # Found objects to dict {cpt : {obj}}
    objects = {i:{} for i in range(len(rows))}
    i = 0
    if columns == ["*"]:
        columns = COLUMNS
    for row in rows:
        obj = {col:"" for col in columns}
        for j in range(len(row)):
            obj[columns[j]] = row[j]
        objects[i] = obj
        i += 1
    return json.dumps(objects)
