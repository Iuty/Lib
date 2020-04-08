from serviceframework import ServiceBase
from serviceframework import ServiceFunc as sf




class Service(ServiceBase):
	def __init__(self):
		ServiceBase.__init__(self)
		pass
	
	def initResource(self):
		
		pass
	
	@sf.cmd
	def start(self,**kwargs):
		
		return {'run':True}
	
	@sf.cmd
	def stop(self,**kwargs):
		
		return {'run':False}
	
	@sf.bll
	def startTrain(self,**kwargs):
		rtn = {'success':False}
		if 'modelname' not in kwargs:
			return rtn
		rtn['success'] = True
		rtn['return'] = self.p_ms.startTrain(**kwargs)
		return rtn
	
	@sf.bll#what is the return?
	def getTrainStatus(self,**kwargs):
		rtn = {'success':False}
		if 'modelname' not in kwargs:
			return rtn
		rtn['success'] = True
		rtn['return'] = self.p_ms.getTrainStatus(**kwargs)
		return rtn
	
	@sf.bll
	def testImage(self,**kwargs):
		rtn = {'success':False}
		if 'modelname' not in kwargs:
			return rtn
		rtn['success'] = True
		rtn['return'] = self.p_ms.testImage(**kwargs)
		return rtn
	
	@sf.bll
	def getModel(self,**kwargs):
		rtn = {'success':False}
		if 'modelname' not in kwargs:
			return rtn
		rtn['success'] = True
		rtn['return'] = self.p_ms.getModelDir(**kwargs)
		return rtn
	
	@sf.bll
	def test(self,**kwargs):
		#ms = test.query.get()
		print (kwargs)




	