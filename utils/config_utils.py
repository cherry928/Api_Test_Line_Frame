import os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, '../config/config.ini')

class Config_utils:

    def __init__(self, config_path=cfgpath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding="utf-8")

    def read_ini(self, sec, option):
        value = self.__conf.get(sec, option)
        return value

    @property
    def get_host_path(self):
        value = self.read_ini('default', 'hosts')
        return value

    @property
    def report_path(self):
        report_path_value = self.read_ini('default', 'report_path')
        return report_path_value

config = Config_utils()

if __name__=='__main__':
    config_u = Config_utils()
    print((config_u.get_host_path))