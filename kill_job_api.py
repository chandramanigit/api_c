#!/usr/bin/python

import os , sys , requests , subprocess 
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
	return "uses: to kill job use /kill?oid=order_id of job"

@app.route('/kill' , methods=['GET' , 'POST'])
def killjob():
	oid = request.args.get('oid')  #fatching the oid from url 
	oid = str(oid)			# converting it to string format may be optional 
	cmd = ('/home/ctmstest/bmcperl/perl force_end_job.pl ' +oid+ ' N < answer.txt')  #answer.txt content Y to run native command without interruption
	p=subprocess.Popen( cmd , stdout=subprocess.PIPE , stderr=subprocess.PIPE , stdin=subprocess.PIPE , shell=True)
	out,err = p.communicate()
	return out

if __name__ == "__main__":
	app.run(host="ctmtest.mylab.com",port=9050)


	
