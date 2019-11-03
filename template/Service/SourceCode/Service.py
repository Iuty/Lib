from serviceframework import ServiceBase
from serviceframework import ServiceFunc as sf

class Service(ServiceBase):
	def __init__(self):
		ServiceBase.__init__(self)
		pass
	
	def initResource(self):
		
		pass
	
	def start(self,**kwargs):
		
		return {'run':True}
	
	
	def stop(self,**kwargs):
		
		return {'run':False}
	pass
