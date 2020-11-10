import configparser
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
    
class Config:
    def __init__(self,path="./Config/Config.conf"):
        self._path = path
        self._config = configparser.ConfigParser()
        self._config.read(self._path)
        pass
        
    def get(self,session,key):
        rtn = None
        try:
            rtn = self._config.get(session,key)
        except Exception as err:
            a = 1
        return rtn
    
    def set(self,session,key,val):
        if not self._config.has_section(session):
            self._config.add_section(session)
        self._config.set(session,key,val)
        
        self.save()
        pass
    
    def save(self):
        with open(self._path,'w') as f:
            self._config.write(f)
        self._config.read(self._path)
        pass
    
    def getSections(self):
        
        rtn = []
        try:
            rtn = self._config.sections()
        except Exception as err:
            print(err+"in Config getSections")
        return rtn
    
    def getOptions(self,section):
        rtn = []
        try:
            rtn = self._config.options(section)
        except Exception as err:
            print(err+"in Config getOption")
        return rtn
    
    def rmSection(self,section):
        self._config.remove_section(section)
        self.save()
        pass
    
    def rmOption(self,section,option):
        self._config.remove_option(section,option)
        self.save()
        pass
    
    def copy(self,target,section,key,defaultvalue):
        v = self._config.get(section,key)
        if not v:
            v = defaultvalue
        try:
            target.set(section,key,v)
        except Exception as err:
            print(err+"in Config copy")
        pass
        