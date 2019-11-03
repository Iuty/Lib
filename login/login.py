from database.mysql import MySql,Column
import datetime


class Login:
	def __init__(self,**kwargs):
		'''
		kwargs:
			host:db host
			user:db user
			password:db password
			projectname:db name
		'''
		host = 'localhost'
		user = 'root'
		password = 'fastcorp'
		projectname = 'test'
		if 'host' in kwargs:
			host = kwargs['host']
		if 'user' in kwargs:
			user = kwargs['user']
		if 'password' in kwargs:
			password = kwargs['password']
		if 'projectname' in kwargs:
			projectname = kwargs['projectname']
		self.mysql = MySql(host,user,password,projectname)
		
		class User(self.mysql.Model):
			ID = Column(PrimaryKey = True,AutoIncrement = True)
			Name = Column(Type = str,NullAble = False)
			PassWord = Column(Type = str,NullAble = False)
			Level = Column(Type = str,Enum = ['Forbid','Common','Super','Admin'],Default = 'Common')
			CreatTime = Column(Type = datetime.datetime)
			InService = Column(Type = datetime.datetime)
			Dist = Column(Type = bytes)
			
			pass
		self.User = User
	
	def addUser(self,name,password,level = 'Common'):
		db0 = self.queryUserByName(name)
		if len(db0)>0:
			raise Exception('Enter duplicate usernames')
		try:
			user.add(value={'Name':name,'PassWord':password,'Level':level,'CreatTime':datetime.datetime.now()})
		except Exception as err:
			raise err
	
	def updateUser(self,name = None,password = None,level = None,inservice = None,dist = None):
		db0 = self.queryUserByName(name)
		if len(db0)>0:
			if password != None:
				user.update(value = {'password':password})
			if level != None:
				user.update(value = {'level':level})
			if inservice != None:
				user.update(value = {'inservice':inservice})
			if dist != None:
				user.update(value = {'dist':dist})
	
	def queryUserByName(self,name = None):
		if name == None:
			raise Exception("Query Has No User Name")
		user = self.User()
		db0 = user.query(where = 'Name = \'{0}\''.format(name),limit='1')
		return db0
	
	def queryUserByDict(self,dict = None):
		user = self.User()
		db0 = user.query(where = 'Dict Like \'{0}%\''.format(dict),limit='1')
		return db0
		pass
	
	
if __name__ == '__main__':
	login = Login(projectname = 'tensorflow')
	user = login.User()
	user.check()
	#login.addUser('t.yu','000001','Admin')
	login.updateUser('t.yu','ff123','Common')
	user.query()
	