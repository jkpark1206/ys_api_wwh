import json
from common.session_init import Session_init
from common.api_demo import ApiDefine
import unittest
from common.Random_str import *
from common.Get_token import Token

class Create_Strategy_Test(Session_init):

    def test_get_strategy_list_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "获取所有策略列表"
        h = {"Authorization": Token()}
        res = ApiDefine().Get_strategy_list(self.session,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)