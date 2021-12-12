#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:33:42 2021

@author: bizzy
"""

# app.py에서 유저와 관련된 기능을 모두 옮기세요.
from flask import Flask,render_template,jsonify,request, redirect, Blueprint

# Blueprint
user = Blueprint("user",__name__)

# DB
user_list=[
    {"name":"elice","password":'1234'},
    {"name":"oliver","password":'1111'},
    {"name":"tony","password":'1257'},
    {"name":"timber","password":'1357'},
]


@user.route("/register" ,methods=["GET"])
def regist_page():
    return render_template("BluePrintRegister.html")

@user.route("/login", methods=["GET"])
def login_page():
    return render_template("BluePrintLogin.html")

@user.route("/register", methods=["POST"])
def register_service():
    id = request.form['username']
    pw = request.form['password']

    user = {'name':id,'password':pw}
    user_list.append(user)
    return redirect("/")

@user.route("/login", methods=["POST"])
def login_service():
    id = request.form['username']
    pw = request.form['password']

    for user in user_list:
        if user['name'] == id and user['password'] == pw:
            return jsonify("유저 로그인!")

    return jsonify("로그인 실패!")
