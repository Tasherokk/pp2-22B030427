import psycopg2
import csv

###

def connect(conn):
    #Connect to the PosgreSQL server
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Taukent2004",
            port = "5432")
        
        #create a cursor
        cur = conn.cursor()

        #execute a statement
        cur.execute('SELECT version()')

        #display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        #Close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
###
        
def createTable(cursor):
    #Create table in PostgreSQL database if such table not exists
    query = """
        CREATE TABLE IF NOT EXISTS postgres.phonebook.phonebook(
            id SERIAL,
            phone VARCHAR(11),
            name VARCHAR(255)
        )
        """
    cursor.execute(query)
    
###

def insertData(cursor, name, phone):
    #Insert data to our table phonebook
    query = f"""
        INSERT INTO postgres.phonebook.phonebook(phone, name)
        VALUES('{phone}', '{name}')
        """
    cursor.execute(query)

###

def getTable(cursor):
    #showing our table
    query = """
        SELECT * FROM postgres.phonebook.phonebook
        """
    cursor.execute(query)
    output = cursor.fetchall()
    for i in output:
        print(i)

###

def updateData(cursor, where, towhat):
    #updating data by name or number
    query = """"""
    if where.isnumeric():
        query = f"""
            UPDATE postgres.phonebook.phonebook
            SET name = '{towhat}'
            WHERE phone = '{where}'
            """
    else:
        query = f"""
            UPDATE postgres.phonebook.phonebook
            SET phone = '{towhat}'
            WHERE name = '{where}'
            """
    cursor.execute(query)

###

def showData(cursor, select, order):
    query = f"""
        SELECT "{select}"
        FROM postgres.phonebook.phonebook
        ORDER BY "{order}"
        """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

###

def deleteData(cursor, name):
    query = f"""
        DELETE FROM postgres.phonebook.phonebook
        WHERE name = '{name}'
        """
    cursor.execute(query)

###

        
conn = None
cursor = None
#connecting
conn = connect(conn)
cursor = conn.cursor()
#creating table
createTable(cursor)
#inserting data into the phonebook
print("Type of query: ")
typ = int(input())

#from console
if(typ == 1):
    print("Amount of data: ")
    n = int(input())
    for i in range (n):
        name = input()
        phone = input()
        insertData(cursor, name, phone)
        
#from csv file
if(typ == 2):
    print("Name of csv file: ")
    s = input()
    dataSet = []
    with open(f"data//{s}.csv") as file:
        reader = csv.reader(file)
        for i in reader:
            dataSet.append(i[0].split(';'))
        dataSet = dataSet[1:]
        for i in dataSet:
            insertData(cursor, i[0], i[1])

#updating table
if(typ == 3):
    print("Change in: ")
    where = input()
    print("To: ")
    towhat = input()
    updateData(cursor, where, towhat)

#showing table with filters
if(typ == 4):
    print("Select: ")
    select = input()
    print("In Order: ")
    order = input()
    showData(cursor, select, order)

#deleting data by name
if(typ == 5):
    print("Name: ")
    name = input()
    deleteData(cursor, name)



if conn is not None:
    #show table
    getTable(cursor)
    conn.commit()
    cursor.close()
    conn.close()
