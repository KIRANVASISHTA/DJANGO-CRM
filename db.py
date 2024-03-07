import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd = 'kiran',
)

# prepare cursor object
cursor = database.cursor()

# create a database
cursor.execute("CREATE DATABASE crmco")

print("Completed the database creation.")