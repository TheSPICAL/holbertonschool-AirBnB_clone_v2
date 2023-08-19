#!/usr/bin/python3
"""
whatever was written after the slash, it will be displayed next to the letter C
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
if somthing was written after the slash that comes after C, it will show on 
        the page after the letter C
    for example if we type /is_cool after /c >>> /c/is_cool ... what will be 
        displayed in that page is C is cool
"""


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return "C %s" % str.replace(text, '_', ' ')


"""
                we are using str.replace because we want to replace all 
                    underscore symbols that are written with a space
                if we dont use the .replace function then /c/is_cool 
                    for example will be displayed like this C is_cool
                but when we tell the function to replace 
                    '_' with ' ' then all underscore symbols will be replaced
                         with space and the example above will display
                             C is cool
"""


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')