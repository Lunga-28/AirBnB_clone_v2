#!/usr/bin/python3
from flask import Flask
"""

"""
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return ('Hello HBNB!')

@app.route('/hbnb')
def hbnb():
    """
    route /hbnb displays
    """
    return ('HBNB')

@app.route('/c/<text>')
def c(text):

    return ("C {}".format(text.replace('_', ' ')))

@app.route('/python')
@app.route('/python/<text>')
def py(text="is cool"):

    return("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def num(n):

    return ("{:d} is a number".format(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
