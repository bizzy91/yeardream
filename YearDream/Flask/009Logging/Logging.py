#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:00:09 2021

@author: bizzy
"""
from flask import Flask,render_template


app = Flask(__name__)

# 404 에러 제어
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('page_not_found.html')

@app.route('/')
def HelloFlask():
    return "Hello, Flask!"

# URL 뒤에 "/wrong" 입력하여 테스트
if __name__ == '__main__':
    app.run()