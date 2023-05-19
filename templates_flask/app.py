from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/units')
def unitList():
    mycursor.execute("SELECT * FROM StudentsPerformance")
    myresult = mycursor.fetchall()
    return render_template('students_performance.html', units=myresult)