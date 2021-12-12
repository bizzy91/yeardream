#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:08:13 2021

@author: bizzy
"""
from flask import Flask


app = Flask(__name__)

@app.route("/")
def FirstApp():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run()
