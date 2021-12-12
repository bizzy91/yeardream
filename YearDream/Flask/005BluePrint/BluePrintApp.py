#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:29:03 2021

@author: bizzy
"""
from flask import Flask,render_template,jsonify,request, redirect
from BluePrintUser import user
from BluePrintBoard import board


app = Flask(__name__)
# App에 API 등록하기
app.register_blueprint(board)
app.register_blueprint(user)

# 기능을 모듈화하고 Blueprint를 등록하세요.
@app.route("/")
def home_page():
    return render_template("BluePrintIndex.html")

if __name__ == '__main__':
    app.run(debug=True)