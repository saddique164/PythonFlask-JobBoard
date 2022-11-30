from flask import Flask, render_template, g
import sqlite3

PATH="db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
    if connection == getattr(g._connection,"None"):
       connection = getattr(g._connection,sqlite3.connect(PATH))
    return connection

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
