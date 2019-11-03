
def getPickleData(path,isDictionary = False):
	"""
	help pass
	"""
	import os,pickle
	if os.path.exists(path):
		file = open(path,'rb')
		rtn = pickle.load(file)
		file.close()
		return rtn
	if isDictionary:
		return {}
	return []

def savePickleData(path,memery):
	"""
	help pass
	"""
	import os,pickle
	f = open(path,'wb')
	pickle.dump(memery,f)
	f.close()