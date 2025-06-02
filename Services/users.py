import psycopg2
from config.connection import connection

def insert_user(name, surname, email, description, course, year, direction, CP, Password):
    conn = connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO "user"."user"(
	    name, surname, email, description, course, year, direction, "CP", password)
	    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (name, surname, email, description, course, year, direction, CP, Password))
        
        
        print("inserted correctly")
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)