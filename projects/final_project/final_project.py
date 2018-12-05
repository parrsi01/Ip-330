import os
import requests
from flask import Flask, redirect, url_for, make_response, session, escape, request, render_template, send_from_directory
import http.client

app = Flask(__name__)

# Set the secret key to some random bytes.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/soccer-xt3/eu/en/schedules/2016-08-18/results.xml?api_key={s9bxp3w4637vu2zzkrufd57f}")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

'''
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
'''

@app.route('/register', methods=['GET','POST'])
def register():

@app.route('/', methods=['GET','POST'])
def index():
    if 'username' in session:
        return render_template('index.html', username=escape(session['username']))
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
       
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/player', methods=['GET','POST'])
def player():
    return render_template('player.html')

@app.route('/league', methods=['GET','POST'])
def league():
    return render_template('league.html')

@app.route('/team', methods=['GET','POST'])
def team():
    return render_template('team.html')

@app.route('/json', methods=['GET','POST'])
def app_json():
    return render_template('json.html')
if __name__ == '__main__':
    app.run() 