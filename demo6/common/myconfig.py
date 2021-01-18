import os
from configparser import ConfigParser

from demo6.common.handle_path import CONFIG


class Config(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.read(file_path, encoding="utf-8")

    def write_conf(self, section, option, value):
        self.set(section=section, option=option, value=value)
        self.write(fp=open(self.file_path, "w"))


conf = Config(os.path.join(CONFIG, "config.ini"))
