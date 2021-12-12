#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:28:04 2021

@author: bizzy
"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

board = [
    {'name': 'elice', 'content': 'my name is elice!'},
    {'name': 'oliver', 'content': 'my name is oliver!'},
    {'name': 'teddy', 'content': 'my name is teddy!'},
    {'name': 'tony', 'content': 'my name is tony!'},
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        board.append({'name': name, 'content': content})
        return redirect('/')
    
    return render_template("JinjaTemplateMix.html", board=board)


if __name__ == "__main__":
    app.run(debug=True)
