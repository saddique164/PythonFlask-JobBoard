from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

@app.route('/')
def jobs():
    return render_template('index.html')

@app.route()
def open_connection():
    connection = getattr(g._connection,"None")
