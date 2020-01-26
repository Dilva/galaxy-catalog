"""
Database access module
"""

import sqlite3


COLUMNS = ["messier_id", "ngc_id", "type", "season", "magnitude", "constellation_en", "constellation_fr", 
"constellation_latin", "ra", "dec", "distance", "size", "discoverer", "year", "image", "constellation_id"]


def get_all_objects():
    """
    Queries database to get all rows. 
    Returns a dict of all objects as {messier_id : {object}}

    Returns :
    dict(dict) : all objects
    """

    c = conn.cursor()
    c.execute("SELECT * FROM objects")
    rows = c.fetchall()

    objects = {k[0]:{} for k in rows}
    for row in rows:
        obj = {col:"" for col in COLUMNS[1:]}
        for i in range(1, len(row)):
            obj[COLUMNS[i]] = row[i]
        objects[row[0]] = obj

    return objects

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

    c = conn.cursor()
    column_query = ",".join(col for col in columns)
    filter_query = ' and '.join(k + "='" + v +"'" for k,v in filter.items())
    #print("SELECT " + column_query + " FROM objects where " + filter_query)
    c.execute("SELECT " + column_query + " FROM objects where " + filter_query)
    rows = c.fetchall()

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
    return objects


# Connection with the database
conn = sqlite3.connect('messier_catalog.db')

#print(get_all_objects())
#print(get_objects(['ngc_id', 'constellation_latin'], {'season':'Autumn', 'type':'Galaxy'}))

# Closing connection
conn.close()