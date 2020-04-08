import requests,json

data = {'testi':1,'testa':'a','cmd':'test,ttt=123,tt=12,t=1','bytes':'uuyytt'}
headers = {'Content-Type':'application/json'}
response = requests.post(url='http://127.0.0.1:7709/servicefunc',headers = headers, data = json.dumps(data))
print (response.text)