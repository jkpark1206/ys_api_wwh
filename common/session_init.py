import requests
import unittest
from common.api_demo import ApiDefine

class Session_init(unittest.TestCase):
    # 实例化一个session类
    def setUp(self) -> None:
        self.session = requests.session()
        # self.session.headers = {"Content-Type":"application/json"}
        # token = ApiDefine().Get_token(self.session)
        # self.session.headers = {"Content-Type":"application/json","Authorization":"Token {}".format(token)}

    def tearDown(self) -> None:
        self.session.close()

