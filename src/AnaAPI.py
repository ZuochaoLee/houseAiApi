#coding:utf-8
#语义解析统一api接口，端口号8788
import subprocess
import os
import json
import logging
import analysis
from flask import Flask,request
app = Flask(__name__)

@app.route('/ana/<text>')
def hello_world(text):
        #param = request.args.get('text')
        param=json.loads(text)
        print param
        # fc=subprocess.check_output('/usr/bin/python analysis.py ' + param['text'],shell=True)
        fc=analysis.run(param['text'])
        # print fc
        return fc #input

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=8788)