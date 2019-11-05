import threading

class MessageQueue:
	def __init__(self):
		self.container = []
		self.lock = threading.Lock()
		pass
		
	def enQueue(self,data):
		self.lock.acquire()
		self.container.append(data)
		self.lock.release()
	
	def deQueue(self):
		self.lock.acquire()
		rtn = None
		if len(self.container) > 0:
			rtn = self.container.pop(0)
		self.lock.release()
		return rtn
	
	def clear(self):
		self.lock.acquire()
		self.container.clear()
		self.lock.release()
		pass