from setuptools import setup

version = "1.0"
try:
    from IutyLib.commonutil.config import Config
    config = Config("./Config.conf")
    ver = config.get("Version","ver")
    subver = config.get("Version","subver")
    version= "{}.{}".format(ver,subver)
except ImportError:
    print("Import Error")


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