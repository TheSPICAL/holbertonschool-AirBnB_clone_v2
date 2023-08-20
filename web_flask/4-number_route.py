#!/usr/bin/python3
"""
learning more about flask
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    return "Python %s" % str.replace(text, '_', ' ')


"""
here we are putting 2 routes, the first /python/ is made so if there is
    nothing after the / symbol it returns the message 'is cool'
    the second route /python/<text> is simmler to the route C above
         that we made, it returns whatever was written after the / symbol
            for example: /python/is_fun the message that it will show is
                Python is fun
"""


@app.route('/number/<int:n>', strict_slashes=False)
def onlynum (n):
        return ("%s is a number" % int(n))

           
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')