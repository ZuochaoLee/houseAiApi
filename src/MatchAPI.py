#coding:utf-8
#匹配度api接口，端口号8780
import subprocess
import os
import logging
from flask import Flask,request
app = Flask(__name__)

@app.route('/pp/<text>')
def hello_world(text):
        #param = request.args.get('text')
        pp=subprocess.check_output('/usr/bin/python ../pp.py "' + text+'"',shell=True)
        return pp #input

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=8780)