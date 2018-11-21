import random
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response
from flask import send_from_directory
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return send_from_directory('static',"shopping_list2.html")
'''
@app.route('/save', methods = ['POST'])
def flask_save():
    #f: file
    f = open("shopping_list.txt", "w")
    shopping_list = request.json.get("shopping_list")
    f.write(shopping_list)
    return "Shopping List Saved"
'''

'''
@app.route('/get', methods=['GET'])
def flask_get():
    #f: file
    f = open("shopping_list.txt", "r")
    content = f.read()
    return jsonify({"shopping_list": content})
'''

if __name__ == '__main__':
    app.run()