import os

DirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF = os.path.join(DirPath,"config")
DATA = os.path.join(DirPath,"datas")
LOG = os.path.join(DirPath,"logs")