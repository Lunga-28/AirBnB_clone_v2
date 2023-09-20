#!/usr/bin/python3
from flask import Flask
"""
intializing flask web app
"""
application = Flask(__name__)

@application.route('/', strict_slashes=False)
def hello_world():
    """
    Display Hello HBNB!
    """
    return ('Hello HBNB!')

if __name__ == "__main__":
    application.run()
