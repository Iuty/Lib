from encription.encription import getfilemd5,des_descrypt,des_encrypt
import os
import random


class FileInfo:
	def __init__(self,path,name):
		self._path = path
		self._name = name
		self._fullpath = os.path.join(path,name)
	
	def isExists(self):
		return True if os.path.exists(self._fullpath) else False
		
	def getMd5(self):
		rtn = ""
		
		if self.isExists():
			rtn = getfilemd5(self._fullpath)
		return rtn
	
	def getSize(self):
		rtn = 0
		if self.isExists():
			rtn = os.path.getsize(self._fullpath)
		return rtn
	
	def getFileStream(self,start,batch = 2000):
		if not self.isExists():
			raise Exception('No such file full path:{}'.format(self._fullpath))
		file = open(self._fullpath,'rb')
		
		size = file.__sizeof__()
		if start > size:
			raise Exception('File is not longer than start cur:{}'.format(start))
		
		file.seek(start)
		end = start + int(batch*random.random())
		if end > size + 1:
			end = size + 1
		rtn = str(file.read(end-start),encoding='UTF-8')
		file.close()
		return rtn
	
	def setFileStream(self,start,bs):
		if start == 0:
			if self.isExists():
				os.remove(self._fullpath)
		
		file = open(self._fullpath,"ab")
		batch = file.write(bs)
		file.close()
		size = self.getSize()
		return size

class DirInfo:
	def __init__(self,path):
		self._path = path
	
	def isExists(self):
		True if os.path.exists(self._path) else False
	
	def getFilesName()
		rtn = []
		if self.isExists():
			files = os.listdir(self._path)
			rtn = [file for file in files if os.path.isfile(self._path+file)]
		return rtn
	
	def getFilesInfo(self,start=0,**kwargs):
		batch = 200
		if 'Size' in kwargs:
			batch = batch//2
		if 'Md5' in kwargs:
			batch = batch//4

		rtn = {'start':start}
		
		files = self.getFilesName()
		rtn['filecount'] = len(files)
		if start > len(files)-1:
			return rtn
		end = start + batch
		
		if (start + batch) >= len(files):
			end = len(files)

		fs = []
		rtn['files'] = fs

		for filename in files[start:end]:
			finfo = {'Name':filename}
			fi = FileInfo(self._path,filename)
			if 'Size' in kwargs:
				finfo['Size'] = fi.getSize()
			if 'Md5' in kwargs:
				finfo['Md5'] = fi.getMd5()
			finfo = {'Name':filename,'Md5':md5,'Size':size}
			fs.append(finfo)
		
		return rtn
	
	def creat(self):
		if not self.isExists():
			os.mkdir(self._path)