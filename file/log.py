from files import StringFile
import os,datetime

class Log(StringFile):
	def __init__(self,root = './/logs//',title = 'log'):
		if not os.path.exists(root):
			p = '.'
			ps = root.split('//')
			for i in range(1,len(ps)-1):
				
				p = p + '//' + ps[i]
				if not os.path.exists(p):
					os.makedirs(p)
		StringFile.__init__(self,root, title)
		pass
	
	def getkwargs(**kwargs):
		argmsg = ''
		for arg in kwargs:
			argmsg = argmsg + '@' + str(arg) + ':' + str(kwargs[arg]) + "; "
		return argmsg

	def appendLog(self,item,message,**kwargs):
		msg = datetime.datetime.now().strftime("%H:%M:%S.%f") + "[" + item + "]:" + message
		if len(kwargs) > 0:
			msg = msg + Log.getkwargs(**kwargs)
		self.append(msg)
		
		pass


class SimpleLog:
	def __init__(self,path = './/logs//'):
		self.log = Log(path)

	def error(self,msg,**kwargs):
		self.log.appendLog('error',msg,**kwargs)

	def info(self,msg,**kwargs):
		self.log.appendLog('info',msg,**kwargs)

	def debug(self,msg,**kwargs):
		self.log.appendLog('debug',msg,**kwargs)

	def warn(self,msg,**kwargs):
		self.log.appendLog('warn',msg,**kwargs)

	def other(self,cmd,msg,**kwargs):
		self.log.appendLog(cmd,msg,**kwargs)