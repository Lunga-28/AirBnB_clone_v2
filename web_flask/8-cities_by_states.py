#!/usr/bin/python3
"""
intialize flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from operator import attrgetter

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """retrieve states from database and render templates based on results"""
    states = []
    all_states = storage.all(State)
    for val in all_states.values():
        states.append(val)
    states = sorted(states, key=attrgetter("name"))
    return render_template('7-states_list.html', state=state)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """retrieve cities by states fro database and render template"""
    states = []
    all_states = storage.all(State)
    for state in all_states.values():
        states.append(state)

    states = sorted(states, key=attrgetter("name"))
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown(self):
    """closes the current session after each request"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
