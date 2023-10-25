#!/usr/bin/python3
"""
intialize flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask
from flask import render_template
from models.state import State
from models.amenity import Amenity
from models import storage
from operator import attrgetter

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """filter out states, amenities from database. Render in html"""
    states = []
    all_states = storage.all(State)
    amenities = []
    all_amenities = storage.all(Amenity)

    for state in all_states.values():
        states.append(state)
    states = sorted(states, key=attrgetter("name"))

    for amenity in all_amenities.values():
        amenities.append(amenity)
    amenities = sorted(amenities, key=attrgetter("name"))

    return render_template('10-hbnb_filters.html', states=states,
            amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
