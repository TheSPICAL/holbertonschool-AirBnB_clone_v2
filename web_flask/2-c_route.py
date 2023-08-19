#!/usr/bin/python3
"""
whatever was written after the slash, and it will be displayed next to C letter
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"

"""
if somthing was written after the slash that comes after C, it will show on the page after the letter C
    for example if we type /is_cool after /c >>> /c/is_cool ... what will be displayed is that page is C is cool
"""

@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """
    the reason it wont be Ciscool because there is a space "C " so it will look like this C is cool 
    """
    return "C " + str(text)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')