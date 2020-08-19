import psycopg2
conn = psycopg2.connect(user="itmadmin", password="Covid@19", database="postgres", host="10.42.81.4", port="5432")
print("Successfully connected!")

cursor = conn.cursor()

cursor.execute("SELECT VERSION();")
version = cursor.fetchone()
print("Connected into - ", version)

cursor.execute("CREATE TABLE py_tbl(id SERIAL PRIMARY KEY, str_col VARCHAR(50),int_col INT);")
print("Table successfully created!")

cursor.execute("INSERT INTO py_tbl(str_col, int_col) VALUES('Hello World!', 110);")
cursor.execute("INSERT INTO py_tbl(str_col, int_col) VALUES('Welcome to ObjectRocket!', 120);")
cursor.execute("INSERT INTO py_tbl(str_col, int_col) VALUES('Greetings!', 130);")

conn.commit()
print("Records Successfully Inserted!”)
conn.close()
