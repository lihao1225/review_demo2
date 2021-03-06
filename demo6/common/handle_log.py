import logging
import os

from demo6.common.handle_path import LOG
from demo6.common.myconfig import conf


class HandleLog(object):

    @staticmethod
    def create_log():
        # 创建收集器设置等级
        my_log = logging.getLogger(conf.get("log", "name"))
        my_log.setLevel(conf.get("log", "level"))
        # 创建输出到控制台，设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log", "sh_level"))
        my_log.addHandler(sh)
        # 创建输出到文件，设置等级
        fh = logging.FileHandler(filename=os.path.join(LOG, "log.log"), encoding="utf-8")
        fh.setLevel(conf.get("log", "fh_level"))
        my_log.addHandler(fh)
        # 设置日志输出格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)
        return my_log


log = HandleLog.create_log()
