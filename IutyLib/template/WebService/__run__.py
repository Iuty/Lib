from flask import Flask,render_template,request,jsonify
import json

from Service import Service

app = Flask(__name__)
service = Service()

host='127.0.0.1'
port = 7709


@app.route('/sendcmd',methods = ['POST',])
def sendcmd():
	data = request.json
	rtn = {'success':False,'reason':'param has no \'cmd\''}
	#print(request.headers)
	if not 'cmd' in data:
		return jsonify(rtn)
	cmd = data['cmd']
	
	rtn = sf.invokeCmd(service,cmd)
	return jsonify(rtn)

@app.route('/servicefunc',methods = ['POST',])
def servicefunc():
	data = request.json
	rtn = {'success':False,'reason':'param has no \'func\''}
	if not 'func' in data:
		return jsonify(rtn)
	rtn = sf.invokeBll(service,data)
	return jsonify(rtn)

if __name__ == '__main__':
	app.run(host=host,port = port,debug=True,use_reloader=False)