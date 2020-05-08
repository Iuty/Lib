from setuptools import setup
import os
version = "1.0"
if os.path.exists("/IutyLib/commonutil/Config.py"):
    print("123")
    from IutyLib.commonutil.config import Config

    config = Config("./Config.conf")
    ver = config.get("Version","ver")
    subver = config.get("Version","subver")
    version= "{}.{}".format(ver,subver)
    pass

setup(
    name="IutyLib",
    version= version,
    #version = ver,
    packages=[
        #"IutyLib",
        "IutyLib.commonutil",
        "IutyLib.database",
        "IutyLib.file",
        "IutyLib.stock",
        "IutyLib.tensor",
        "IutyLib.monitor",
        ]
)