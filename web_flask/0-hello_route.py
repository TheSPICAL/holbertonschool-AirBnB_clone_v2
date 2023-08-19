#!/usr/bin/python3
"""
Hello HBNB! message shows on the localhost, port 5000.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello HBNB!"

if __name__ == "__main__":
app.run(debug=True, port=5000)