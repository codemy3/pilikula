from flask import Flask, render_template
from data import places  

app = Flask(__name__)

@app.route('/')
def home():
    """
    Route to display the homepage with a list of places.
    """
    return render_template('index.html', places=places)

@app.route('/place/<int:place_id>')
def place_detail(place_id):
    """
    Route to display details of a specific place using its unique ID.
    """
    # Search for the place with the given ID
    place = next((place for place in places if place['id'] == place_id), None)
    if place:
        return render_template('place.html', place=place)
    else:
        # Render a custom 404 page if the place is not found
        return render_template('404.html', message="Place not found!"), 404

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)


