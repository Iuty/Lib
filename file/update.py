from task.tasks import TaskProxy,Task
import requests,json

class Server:
	"""
	client download from server
	"""
	def getFullPath(namespace,path):
		if namespace == None:
			#root is None => path is full path
			return os.path.join("./" ,path)
		else:
			#root not None => path is rel path,find root at os.path
			if not namespace in os.sys.path:
				raise Exception("{} not in system path".format(namespace))
			return os.path.join(os.sys.path[namespace],path)

	def getDir(namespace,path,filter = [],choise = []):
		rtn = {"exists":False}
		fullpath = getFullPath(namespace,path)
		if os.path.exists(path):
			rtn["exists"] = True
			rtn["dirs"] = []
			rtn["files"] = []
			for root,dirs,files in os.walk(fullpath):
				for dir in dirs:
					if root != path:
						continue
					rtn["dirs"].append(dir)
				for file in files:
					if root != path:
						continue
					ext = file.split('.')[-1]
					if len(filter) > 0:
						if ext in filter:
							continue
					if len(choise) > 0:
						if not (ext in choise):
							continue
					rtn["files"].append(file)

		return rtn

	def getFile(namespace,path,filename,start,slice = 1000):
		rtn = {"exists":False}
		dirpath = getFullPath(namespace,path)
		fpath = os.path.join(dirpath,filename)
		if os.path.exists(fpath):
			rtn["exists"] = True
			
			rtn["start"] = start
			
			f = open(fpath,"rb")
			f.read(start)
			rtn["data"] = f.read(slice)

			rtn["surplus"] = len(f.read())
		return rtn

	"""
	client upload to server
	"""
	def setFile(root,path,filename,start,data,format = "utf-8"):
		rtn = {"success":False}
		if root in os.sys.path:
			dpath = os.path.join(os.sys.path[root],path)
			if not os.path.exists(dpath):
				os.mkdir(dpath)
			fpath = os.path.join(dpath,filename)
			f = open("fpath","ab+")
			if len(f.read()) != start:
				rtn['err'] = "start is not match with local file"
				return rtn
			f.write(bytes(data,format))
			f.close()
			rtn['success']=True
		return rtn

	pass

class TransFile(Task):
	_format = "utf-8"
	_local = "./"
	def __init__(self,remote,path,filename):
		Task.__init__(self)
		self._remote = remote
		self._path = path
		self._filename = filename
		pass

	@property
	def Name(self):
		return os.path.join(self._local,self._path,self._filename)

	def writeFile(self,data,start):
		rtn = True
		dpath = os.path.join(self._local,self._path)
		if not os.path.exists(dpath):
			os.mkdir(dpath)
		fpath = os.path.join(dpath,self._filename)
		f = open("fpath","ab+")
		if len(f.read()) != start:
			rtn = False

		f.write(bytes(data,self._format))
		f.close()
		return rtn

	def readFile(self,start,lenth):
		fname = os.path.join(self._local,self._path,self._filename)
		if not os.path.exists(fname):
			return bytes('',self._format)
		f = open(fname,"rb")
		f.read(start)
		data = f.read(lenth)
		f.close()
		return data

	


class UploadClient(TaskProxy):
	def __init__(self,url = "127.0.0.1:7000/filesys"):
		self._url = url
		TaskProxy.__init__(self)
		pass
	
	def getDir(self,remote,path):


	def runTask():
		self._task.setFile(self._url)
		pass

class DownloadClient(TaskProxy):
	def __init__(self,url = "127.0.0.1:7000/filesys"):
		self._url = url
		TaskProxy.__init__(self)
		pass
		
	def runTask():
		self._task.getFile()
		pass


