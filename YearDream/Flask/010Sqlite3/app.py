#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:57:08 2021

@author: bizzy
"""

from flask import Flask, render_template, request, url_for, redirect
import sqlite3


app = Flask(__name__)

# DB 연결
conn = sqlite3.connect('./database.db')
# Table 생성
conn.execute('CREATE TABLE IF NOT EXISTS Board (name TEXT, context TEXT)')
value = [['Elice', 15], ['Dodo', 16], ['Checher', 17], ['Queen', 18]]
for i in range(4):
    conn.execute(f"INSERT INTO Board(name, context) VALUES('{value[i][0]}', '{value[i][1]}')")
conn.commit()
conn.close()


@app.route('/')
def board():
    con = sqlite3.connect("./database.db")
    cur = con.cursor()
    cur.execute("select * from Board")
    rows = cur.fetchall()
    con.close()
    print("DB:")
    for i in range(len(rows)):
            print(rows[i][0] + ':' + rows[i][1])
    return render_template('board.html', rows = rows)

@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        result = request.form['search']
        # 데이터베이스를 연결하세요.
        con = sqlite3.connect("./database.db")

        # cursor 객체를 만드세요.
        cur = con.cursor()

        # Board 테이블에서 요청받은 result가 있는지 찾는 쿼리를 실행하세요.
        cur.execute(f"SELECT * FROM Board WHERE name='{result}' or context='{result}'")
        
        # 쿼리 실행 결과를 rows 변수에 저장하세요.
        rows = cur.fetchall()

        # DB의 연결을 해제하세요.
        con.close()
        
        print("DB:")
        for i in range(len(rows)):
            print(rows[i][0] + ':' + rows[i][1])
        return render_template('search.html', rows = rows)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)