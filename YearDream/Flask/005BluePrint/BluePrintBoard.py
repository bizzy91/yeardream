#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:31:08 2021

@author: bizzy
"""
from flask import render_template, jsonify, request, redirect, Blueprint

# Blueprint
board = Blueprint('board', __name__)

# DB
board_list= []


@board.route("/board",methods=["GET"])
def board_page():
    return render_template("BluePrintBoard.html")

@board.route("/board" ,methods=["POST"])
def resgist_service():
    name = request.form['usernmae']
    content = request.form['content']
    data = {'name':name,'content':content}
    board_list.append(data)

    return redirect("/board")

@board.route("/board/<id>")
def edit_board(id):
    content=request.form['content']
    board_list[id+1]['content'] = content
    return redirect("/board")
