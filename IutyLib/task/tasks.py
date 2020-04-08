import datetime,os
from abc import abstractmethod
from show.console import showProcessInConsole
from timeutil import getTimeTamp
from mutithread.threads import SubThread
import commonutil.config

class TaskProxy:
    """
    for single thread
    """
    def __init__(self):
        self.__todo__ = []
        self.__finished__ = []
        self._task_ = None
        pass

    def addTask(self,task):
        self.__todo__.insert(0,task)
        pass

    def removeTask(self,taskname):
        rtn = False
        for ti in self.__todo__:
            if ti._name_ == taskname:
                self.__todo__.remove(ti)
                rtn = True
                break
        return rtn
    
    def getTask(self):
        rtn = None
        if len(self.__todo__) > 0:
            rtn = self.__todo__.pop()
        return rtn
    
    def finTask(self,tsk):
        self.__finished__.insert(0,tsk)
        return len(self.__finished__)
    
    @property
    def Process(self):
        p = 0
        if (len(self.__todo__) + len(self.__finished__)) > 0:
            p = len(self.__finished__)/(len(self.__todo__) + len(self.__finished__))
        return p
    
    def runTask(self):
        pass
    pass

class TaskItem:
    """
    
    """
    _start = 0
    _to = 1
    def __init__(self,name,type):
        self._name = name
        self._type = type
        pass
    
    @property
    def Start(self):
        return self._start
    
    @Start.setter
    def Start(self,v):
        self._start = v
        pass
    
    @property
    def To(self):
        return self._to
    
    @To.setter
    def To(self,v):
        print(v)
        self._to = v
        pass
        
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Type(self):
        return self._type
    
    @property
    def Process(self):
        return self._start/(self._start+self._to)
    
    pass



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
        
class SubTask(SubThread):
    def __init__(self,notice = None,args = ()):
        SubThread.__init__(self,self.taskFunc,notice = None,args = ())
        pass
    
    #virtual func
    def taskFunc(*args):
        pass
    
    pass