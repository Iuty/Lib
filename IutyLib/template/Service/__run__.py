from flask import Flask,render_template,request,jsonify
import json
from framework.serviceframework import ServiceFunc as sf
from Service.Service import Service

app = Flask(__name__)
service = Service()

host='127.0.0.1'
port = 8710


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

if __name__ == '__main__':
	
	app.run(host=host,port = port,debug=True,use_reloader=False)
	