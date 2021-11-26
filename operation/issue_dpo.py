# coding:utf-8
import datetime

from core.result_base import ResultBase
from api.issue_dpo import Issue_dpo
from common.logger import run_log as logger
from common.read_data import data
import urllib3

urllib3.disable_warnings()

file_path = '/Users/rootant/PycharmProjects/test/data/issue.json'
header = data.getJson_value('Headers', '/Users/rootant/PycharmProjects/test/data/user.json')
issue_verify_data = data.getJson_value('issue_verify_data', filename=file_path)
get_attachment_data = data.getJson_value('get_attachment_data',filename=file_path)

def get_attachment_id(token):
    result = ResultBase()
    parameters = get_attachment_data
    res = Issue_dpo.issue_document_list(params=parameters,headers=header,cookies= token)
def issue_verify_info(token):
    result = ResultBase()
    issue_data = issue_verify_data
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    issue_data['contract']['effective_date'] = today.strftime('%Y-%m-%d')


    res = Issue_dpo.issue_verify(json=issue_data, headers=header, cookies=token)


if __name__ == '__main__':
    data = issue_verify_data
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    data['contract']['effective_date'] = today.strftime('%Y-%m-%d')
    data['contract']['due_date'] = tomorrow.strftime('%Y-%m-%d')
    print(data['contract'])
