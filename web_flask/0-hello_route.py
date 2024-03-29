#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:15:54 2020
@author: Robinson Montes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
