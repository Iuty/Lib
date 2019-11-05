import requests,json
import threading

class Port:
	def __init__(self,ip,port):
		self._ip = ip
		self._port = port
		self._lock = threading.Lock()
	
	def sendcmd(self,cmd):
		self._lock.acquire()
		url = 'http://'+self._ip+':'+str(self._port)+'/sendcmd'
		headers = {'Content-Type':'application/json'}
		data = {'cmd':cmd}
		response = requests.post(url=url,headers = headers, data = json.dumps(data))
		rtn = json.loads(response.text)
		self._lock.release()
		return rtn
	