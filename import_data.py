import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Students")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS Students.StudentsPerformance (
    id INTEGER NOT NULL,
    gender VARCHAR(30) ,
    race_ethnicity VARCHAR(30),
    parental_level_of_education VARCHAR(30),
    lunch VARCHAR(30),
    test_preparation_course VARCHAR(30),
    math_score INTEGER,
    reading_score INTEGER,
    writing_score INTEGER,
    img VARCHAR(30),
    PRIMARY KEY (id)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM Students.StudentsPerformance")
mydb.commit()

#Read data from a csv file
students_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
students_data = students_data.fillna('Null')
print(students_data.head(20))

#Fill the table
for i,row in students_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO Students.StudentsPerformance VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM Students.StudentsPerformance")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)