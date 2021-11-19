# coding:utf-8

import json
from configparser import ConfigParser
from common.logger import run_log as logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():

    def __init__(self):
        pass

    def load_json(self, file_path):
        # logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        # logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def getJson_value(self, key, filename):

        if filename == None:
            return "文件为空"
        jsonData = self.load_json(filename)
        if key == None:
            getJsonValue = "参数错误"
        else:
            getJsonValue = jsonData.get(key)
        return getJsonValue

    def load_ini(self, file_path):
        # logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data


data = ReadFileData()
if __name__ == '__main__':
    print(data.getJson_value('Headers','/Users/rootant/PycharmProjects/test/data/user.json'))
    print(data.load_ini('/Users/rootant/PycharmProjects/test/config/setting.ini')['host']['api_root_url'])