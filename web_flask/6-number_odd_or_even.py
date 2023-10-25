#!/usr/bin/python3
"""
intialize flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_hello():
    return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Return C is <text>"""
    return "C is {}".format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is fun'):
    """displays Python is '<text>', defaults to 'Python is cool"""
    return "Python is {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def check_num(n):
    """check if 'n' is a number"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def render_num(n):
    """render a number template"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """Render page for even/odd numbers"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
