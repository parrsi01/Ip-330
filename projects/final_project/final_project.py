import os
import requests
from flask import Flask, redirect, url_for, make_response, session, escape, request, render_template, send_from_directory
import psycopg2
import records

app = Flask(__name__)


def get_data_from_db(query: str) -> list:
    try:
        conn = psycopg2.connect(
            user="parrsi01", host="knuth.luther.edu", port=5432, dbname="cars")
    except:
        raise ConnectionError("Could not connect to the database")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    pass

@app.route('/main', methods=['GET','POST'])
def main():
    pass

@app.route('/final', methods=['GET','POST'])
def final():
    pass




if __name__ == '__main__':
    app.run() 