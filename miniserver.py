#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Test icin basit HTTP Server deploymenti
"""

__version__ = '1.0'
__author__ = 'Pınar Karga'

from flask import Flask, Response
from main import is_http_ok

app = Flask(__name__)

@app.route('/200')
def index():
    return Response("this is 200", status=200)

@app.route('/not200')
def status_test():
    return Response("401 test", status=401)

def main():
    app.run(port=8080, debug=False)

if __name__ == '__main__':
    main()
