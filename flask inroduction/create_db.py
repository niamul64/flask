import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)
my_cursor=mydb.cursor()


#to create new database
#my_cursor.execute("CREATE DATABASE inputdb") #test is the name of the data base which we are going to create

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
