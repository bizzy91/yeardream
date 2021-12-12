#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:13:13 2021

@author: bizzy
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def RenderTemplate():
    return render_template('RenderTemplate.html')


if __name__ == "__main__":
    app.run()
