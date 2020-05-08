from IutyLib.commonutil.config import Config
import datetime

if __name__ == "__main__":
    dt = datetime.datetime.now()
    yy = dt.strftime("%y")
    mmdd = dt.strftime("%m%d")
    HHMM = dt.strftime("%H%M")

    config = Config("./Config.conf")
    
    config.set("Version","subver","{}.{}.{}".format(yy,mmdd,HHMM))
    pass