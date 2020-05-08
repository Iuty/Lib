from setuptools import setup
from IutyLib.commonutil.Config import Config

config = Config("./Config.conf")
ver = config.get("Version","ver")
subver = config.get("Version","subver")

setup(
    name="IutyLib",
    version= "{}.{}".format(ver,subver),
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