# save this as app.py
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
mycursor.execute("CREATE DATABASE IF NOT EXISTS STUDENTS_PERFORMANCE")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS STUDENTS_PERFORMANCE.DATA (
    ID INTEGER NOT NULL,
    gender VARCHAR(30),
    race_ethnicity VARCHAR(30),
    parental_level_of_education VARCHAR(30),
    lunch VARCHAR(30),
    test_preparation_course VARCHAR(30),
    math_score INTEGER,
    reading_score INTEGER,
    writing_score INTEGER,

    
    PRIMARY KEY (ID)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM STUDENTS_PERFORMANCE.DATA")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO STUDENTS_PERFORMANCE.DATA VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM STUDENTS_PERFORMANCE.DATA")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)