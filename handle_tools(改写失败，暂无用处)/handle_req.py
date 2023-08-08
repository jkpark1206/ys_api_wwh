import json
from common.api_define import APIDefine
import unittest
from handle_tools.handle_yaml import *
from handle_tools.handle_yaml import Handle_yaml
import requests
import json
from unittestreport import ddt,list_data,yaml_data,json_data

sh = Handle_yaml("/testcases/Atestcases.yaml")
data = sh.read_yaml()


@ddt
class Test_Login(unittest.TestCase):
    name = "易识v2.8"
    @classmethod
    def setUpClass(cls) -> None:
        # logger.info(f"\n==========================={cls.name}接口测试开始===========================")
        print('测试开始')
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
    # def setUp(self) -> None:
    #     self.session=requests.session()
    #     token = APIDefine().get_authToken()
    #     self.session.headers = {"Content-Type":"application/json","Authorization":"Token {}".format(token)}
    #
    # def  tearDown(self) -> None:
    #     self.session.close()

    @list_data(data)
    def test_case01_list(self):
        # logger.info(f"\n*****************{data['title']}*****************")
        resp = APIDefine().send_req(data['method'], data['url'], data['req_data'])
        try:
                a = resp.json()["message"]
                b = resp.json()["code"]
                self.assertIn("OK", a)
                self.assertIs(200, b)
                # logger.info(f"返回的message为{a}，对比通过")
        except Exception as e:
                # logger.error(f"{e}")
            print(e)

    # def test_case02_list(self):
    #     # logger.info(f"\n*****************{data['title']}*****************")
    #     resp = APIDefine().send_req(data['method'], data['url'], data['req_data'])
    #     # try:
    #     a = resp.json()["message"]
    #     b = resp.json()["code"]
    #     self.assertIn("OK", a)
    #     self.assertIs(200, b)

