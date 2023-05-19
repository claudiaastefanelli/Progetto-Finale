# save this as hello.py
from flask import Flask
import mysql.conector 
import pandas as pd 
import flask as render_template


app = Flask(__name__)


@app.route("/")
def hello():