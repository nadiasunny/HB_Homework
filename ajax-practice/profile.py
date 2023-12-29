import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    
    return render_template("index.html")


@app.route('/api/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.json['name']
    age = request.json['age']
    occupation = request.json['occupation']
    #salary = request.json['salary']
    #education = request.json['education']
    #state = request.json['state']
    #city_type = request.json['city']
    #garden = request.json['garden']
    #tv = request.json['tv']
    # TODO: get the values from the rest of the form
    # Add them to jsonify
    
    return jsonify({'fullname': fullname, 
                    'age': age,
                    'occupation': occupation,
                    #'salary': salary,
                    #'education': education,
                    #'state': state,
                    #'city_type': city_type,
                    #'garden': garden,
                    #'tv': tv
                    })





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
