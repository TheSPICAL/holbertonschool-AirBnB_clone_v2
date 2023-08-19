#!/usr/bin/python3

from flask import Flask

"""
'Hello HBNB!" message shows on the localhost, port 5000
"""
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)