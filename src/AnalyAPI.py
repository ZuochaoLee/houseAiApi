#coding:utf-8
#语义解析api接口，端口号8778
import subprocess
import os
import logging
from flask import Flask,request
app = Flask(__name__)

@app.route('/fc/<text>')
def hello_world(text):
        #param = request.args.get('text')
        fc=subprocess.check_output('/usr/bin/python ../ree.py ' + text,shell=True)
        return fc #input

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=8778)