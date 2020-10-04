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
        return self._config.get(session,key)
    
    def set(self,session,key,val):
        if not self._config.has_section(session):
            self.add_section(session)
        self._config.set(session,key,val)
        
        with open(self._path,'w') as f:
            self._config.write(f)
        self._config.read(self._path)
        pass