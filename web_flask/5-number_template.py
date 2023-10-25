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

@app.route('/number/<int:num>', strict_slashes=False)
def check_num(num):
    """check if 'num' is a number"""
    return "{:d} is a number".format(num)

@app.route('/number_template/<int:num>', strict_slashes=False)
def render_num(num):
    """render a number template"""
    return render_template('5-number.html', num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
