#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:24:55 2021

@author: bizzy
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# URL 뒤에 ?name=bizzy 입력
@app.route("/", methods=["GET"])
def Request():
    # GET 방식에서 데이터를 가져오는 request.args를 사용해서 name을 가져오고 JSON 형태로 반환하세요.
    name = request.args.get('name')
    return jsonify(name)

        
if __name__ == "__main__":
    app.run()
