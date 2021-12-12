#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:18:42 2021

@author: bizzy
"""
from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def Jsonify():
    data = {
        "name": "bizzy",
        "gender": "male"
    }
    # return data
    return jsonify(data)


if __name__ == "__main__":
    app.run()