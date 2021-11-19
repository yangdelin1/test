# coding:utf-8
from core.result_base import ResultBase
from api.user import user
from common.logger import run_log as logger
from common.read_data import data

header = data.getJson_value('Headers','/Users/rootant/PycharmProjects/test/data/user.json')
user_edit_data = data.getJson_value('edit_user','/Users/rootant/PycharmProjects/test/data/user.json')

def get_edit_user_info():
    '''
    获取编辑User的信息
    :return:
    '''
    result = ResultBase()
    res = user.edit_user(json=user_edit_data,headers=header)
    result.success = False
    if res.json()['code'] ==0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()['data']
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))

    return result

# if __name__ == '__main__':
#     print(get_edit_user_info())