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
        
        with open(self._path,'w') as f:
            self._config.write(f)
        self._config.read(self._path)
        pass