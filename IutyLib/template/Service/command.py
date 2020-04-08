import requests,json

url = 'http://127.0.0.1:8710/sendcmd'
while True:
	print("Input command here('quit' 4 exit,getcmds 4 get all commands):")
	cmd = input()
	if cmd == 'quit':
		break
	data = {'cmd':cmd}
	#data = {'cmd':'doTrain,namespace= ,name= '}
	#data = {'cmd':'stopTrain'}
	headers = {'Content-Type':'application/json'}
	response = requests.post(url=url,headers = headers, data = json.dumps(data))
	print (response.text)