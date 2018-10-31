from flask import Flask
from flask import redirect, url_for
from flask import request, make_response
from flask import render_template
import math

app = Flask(__name__)


def is_prime(n: int) -> bool:
    x = True 
    for i in range(2, n):
        if n%i == 0:
            x = False
            break
    if x:
        print("number is prime")
        return n
    else:
        print("number is not prime")
        return n
    raise NotImplementedError

def get_n_primes(n: int) -> list:
    a = is_prime(n)
    for i in range(1, a+1):
        is_prime(i)
    return n
    raise NotImplementedError


@app.route('/')
def index():
    if request.method == 'GET':
        num = request.args.get('number')
        if num is None:
            return render_template('ask.html')
        else:
            return render_template('prime_table.html')
    else:
        response = make_response(redirect(url_for('index')))
        if request.form.get('number'):
            response.set_cookie('number', '', expires=0)
        else:
            num = request.form.get('number')
            response.set_cookie('number', num)
        return response

    raise NotImplementedError

@app.route('/<int:n>',methods=['GET','POST'])
def get_primes(n):
    if request.method == 'GET':
        number = n
        return render_template('prime_table.html', get_n_primes=get_n_primes(n), number=n)
    raise NotImplementedError

@app.route('/ask', methods=['GET','POST'])
def ask_a_number():
    if request.method == 'GET':
        return render_template('ask.html')    
    raise NotImplementedError

if __name__ == '__main__':
    app.run()
