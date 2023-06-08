#!/usr/bin/env python3
"""A New App using Flask"""


from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """A base Route of the App"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

