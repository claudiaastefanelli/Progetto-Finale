from flask import render_template
from flask import Flask
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""

)

mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/')
def unitList():
    mycursor.execute("SELECT * FROM STUDENTS_PERFORMANCE.DATA")
    myresult = mycursor.fetchall()
    return render_template('students_performance.html', DATA=myresult)
    

