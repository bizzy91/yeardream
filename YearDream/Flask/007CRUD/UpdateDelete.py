#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:34:50 2021

@author: bizzy
"""
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

board = []

@app.route('/')
def index():
    return render_template('list.html', rows = board)

@app.route('/add', methods = ['POST'])
def add():
    print(request.method)
    if request.method == 'POST':
        board.append([request.form['name'], request.form['context']])
        return redirect(url_for('index'))
    else:
        return render_template('list.html', rows=board)

@app.route('/delete/<int:uid>')
def delete(uid):
    board.remove(board[uid-1])
    return redirect(url_for('index'))

@app.route('/update/<int:uid>', methods=['GET','POST'])
def update(uid):
    if request.method =='POST':
        # board 리스트에서 uid번 째에 해당하는 원소를 입력받은 name과 context로 수정한다.
        board[uid-1] = [request.form['name'], request.form['context']]
        return redirect(url_for('index'))
    else:
        return render_template('update.html',index=uid,rows=board)


if __name__ == '__main__':
    app.run(debug=True)