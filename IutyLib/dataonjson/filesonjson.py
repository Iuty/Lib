import requests,json
from encription.encription import getfilemd5,des_descrypt,des_encrypt
from commonutil.queue import MessageQueue as Mq
import os
from file.fileinfo import FileInfo,DirInfo
from dataonjson.port import Port


class DirOnJson:
	queue_check = Mq()
	queue_diff = Mq()
	def __init__(self,jsonport,root,path):
		self._port = jsonport
		self._dir = DirInfo(root,path)
	
	def getRemoteFilesMd5(self):
		index = 0
		
		while True:
			data = {'root':self._root,'path':self._path,'index':index}
			response = port.sendcmd(data)
			#data:{'success':True,'filecount':10,'files':[{Name:file1,Md5:md51,Size:size1},{Name:file2,Md5:md52,Size:size2}]}
			
			if not response['success']:
				raise Exception("Operation error in check Dir")
			if len(response['files']) > 0:
				for rf in response['files']:
					self.queue_check.enQueue(rf)
			if (len(response['files']) + index) == (response['filecount'] - 1):
				break
			index += len(data_return['files'])
	
	def checkPullFiles(self):
		while len(self.queue_check) > 0:
			fri = self.queue_check.deQueue()
			fli = FileInfo(self._dir._fullpath ,fri['Name'])
			if fli.getMd5() != fri['Md5']:
				self.queue_diff.enQueue(fri)
		pass
	
	def getRemoteFile(self,filename):
		start = 0
		while True:
			data = {}