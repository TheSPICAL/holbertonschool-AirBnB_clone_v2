#!/usr/bin/python3
"""
adding a /hbnb page to our site that shows the message HBNB"
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')