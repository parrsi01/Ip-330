from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import make_response


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_user():
    if request.method == 'GET':
        user_name = request.get_cookie('username')
        if user_name:
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        response = make_response(redirect(url_for('hello_user')))

        username = request.form.get('username')
        response.set_cookie('username', username)

        return respose

if __name__ == '__main__':
    app.run()