import os

DIRPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(DIRPATH,"datas")
print(DATA)