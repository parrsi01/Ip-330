import os
from flask import Flask, redirect, url_for, make_response, session, escape, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import http.client
import json


app = Flask(__name__)

# Set the secret key to some random bytes.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)




class SoccerDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    country = db.Column(db.Integer, primary_key=True)

    def __init__(self):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.team = team
        self.league = league
        self.complete = False

    def __repr__(self):
        return str(self.firstname)
    
    def returnDatabase(self):
        return str(self.firstname), str(self.lastname), str(self.overall), str(self.team),str(self.league)



#Populates data for sql table
def populate():
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", "https://api.sportradar.us/soccer-{access_level}{version}/{league_group}/{language_code}/schedules/live/results.{format}?api_key= g5my63s4henathevny9npqem")

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return data
@app.route('/temp', methods=['GET','POST'])
def temp():
    x = populate()
    return str(x)

@app.route('/register', methods=['GET','POST'])
def register():
    pass

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
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('player'))

@app.route('/league', methods=['GET','POST'])
def league():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('league'))

@app.route('/team', methods=['GET','POST'])
def team():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('team'))

@app.route('/database', methods=['GET','POST'])
def database():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('database'))

@app.route('/json', methods=['GET','POST'])
def app_json():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for(''))



if __name__ == '__main__':
    app.run() 