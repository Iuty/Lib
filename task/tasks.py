import datetime,os
from abc import abstractmethod
from show import showProcessInConsole
from timeutil import getTimeTamp
import config

class SingleTaskManager:
	def __init__(self,name,startmark,filepath = './/config//'):
		self.name = name
		self.startmark = startmark
		self.__filepath__ = filepath + 'task_' + name + '.pkl'
		
		self.needinit = not os.path.exists(self.__filepath__)
		self.__tasks__ = []

		self.__taskhandles__ = []
		if self.needinit:

			self.__tasktodo__ = []
			self.__finished__ = []
			self.__savedata__ = {'startmark':datetime.datetime(2019,6,11,16),'todos':self.__tasktodo__,'finished':self.__finished__}
			self.saveData()
		else:
			self.__savedata__ = config.getPickleData(self.__filepath__)
			
			self.__tasktodo__ = self.__savedata__['todos']
			self.__finished__ = self.__savedata__['finished']
		pass
	
	
	def saveData(self):
		config.savePickleData(self.__filepath__,self.__savedata__)
	
	@property
	def Remains(self):
		todocount = 0
		for todo in self.__tasktodo__:
			todocount += len(todo)
		return todocount
	
	@property
	def Starts(self):
		return self.__savedata__['startmark']
	
	def regeditTask(self,taskname,taskhandle):

		self.__tasks__.append(taskname)
		self.__taskhandles__.append(taskhandle)
		if self.needinit:
			self.__tasktodo__.append([])
			self.saveData()
		pass
		
	def initTask(self,args):
		for todo in self.__tasktodo__:
			todo.clear()
		self.__finished__.clear()
		for arg in args:
			self.__tasktodo__[0].append(arg)
		self.__savedata__['starts'] = datetime.datetime.now()
		self.__savedata__['startmark'] = getTimeTamp(self.startmark)
		
		self.saveData()
		pass
		
	def runTask(self):
		rtn = {'run':True}
		if self.Remains == 0:
			rtn['run'] = False
			return rtn
		
		finished = len(self.__finished__)
		for i in range(0,len(self.__tasks__)):
			if len(self.__tasktodo__[i]) > 0:
				arg = self.__tasktodo__[i].pop(0)
				self.__taskhandles__[i].__call__(arg)
				target = self.__finished__
				if i != (len(self.__tasks__)-1):
					target = self.__tasktodo__[i+1]
				target.append(arg)
				self.saveData()
				#print(self.__savedata__)
				#print ('taskfinish -> {0}, arg -> {1}'.format(self.__tasks__[i],arg))
		if len(self.__finished__) != finished:
			kwargs = {}
			for i in range(0,len(self.__tasks__)):
				if len(self.__tasktodo__[i]) > 0:
					kwargs[self.__tasks__[i]] = len(self.__tasktodo__[i])
			kwargs['Finish'] = len(self.__finished__)
			showProcessInConsole(self.name,self.__savedata__['starts'],self.Remains,(self.Remains+len(self.__finished__)),**kwargs)
		return rtn