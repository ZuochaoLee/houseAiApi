#coding:utf-8
#问答库api接口，端口号8779
import subprocess
import os
import logging
from flask import Flask,request
app = Flask(__name__)

@app.route('/qa/<text>')
def hello_world(text):
        #param = request.args.get('text')
        qa=subprocess.check_output('/usr/bin/python ../qa.py ' + text,shell=True)
        return qa #input

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=8779)