# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 16:12:03 2025

@author: gl-ca
"""

from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/about")
def about():
    return "Página sobre"

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__=="__main__":
    app.run(debug=True)