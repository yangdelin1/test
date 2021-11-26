# coding:utf-8
import os
from core.rest_client import RestClient
from common.read_data import data
import urllib3
urllib3.disable_warnings()

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

class Issue_dpo(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Issue_dpo, self).__init__(api_root_url, **kwargs)

    def upload_document(self,**kwargs):
        return self.post("/ucenter/document",**kwargs)

    def issue_document_list(self,**kwargs):
        return self.get("/ucenter/document/dpo/list",**kwargs)

    def issue_verify(self,**kwargs):
        return self.post("/obligation/enterprise/letter/issue.json/verify",**kwargs)

    def issue_submit(self,**kwargs):
        return self.post("/obligation/enterprise/letter/issue.json/submit",**kwargs)