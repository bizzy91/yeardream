#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:49:05 2021

@author: bizzy
"""
from flask import Flask, render_template, redirect, request


app = Flask(__name__)

# Data 
my_fruit = '수박'
# Data (List)
fruit_list = ['수박']
# Data (Dictionary)
lecture_info = {'name': 'Flask 기초', 'time': '2week',
                'level': 'middle', 'lan': 'python'}


@app.route("/", methods=["GET", "POST"])
def home():
    # 버튼 동작
    if request.method == 'POST':
        # "JinjaTemplate.html"의 form 태그에서 name="fruit"인 데이터를 요청한다.
        input_fruit = request.form['fruit']
        # input_fruit에 저장한다.
        fruit_list.append(input_fruit)
        return redirect('/')

    return render_template(
        "JinjaTemplate.html", 
        fruit=my_fruit,
        fruit_list=fruit_list,
        lecture_info=lecture_info
        )

if __name__ == "__main__":
    app.run(debug=True)
