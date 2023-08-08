import unittest
from common.session_init import Session_init
import json
from common.api_demo import ApiDefine
from config.config import local_config

class Change_passwd_test(Session_init):

    @unittest.skip
    def testcase_passwd_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "成功修改密码"
        data = {
        "username":local_config.Username,
        "password":local_config.Passwd,
        "message":"安般"
            }
        res = ApiDefine().Change_Passwd(self.session,data)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('OK',a)
        self.assertEqual(200,b)


    @unittest.skip
    def testcase_passwd_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "修改密码失败-用户名错误"
        data = {
        "username":"zz",
        "password":local_config.Passwd,
        "message":"安般"
            }
        res = ApiDefine().Change_Passwd(self.session,data)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('用户或密保参数错误！',a)
        self.assertEqual(2004,b)


    @unittest.skip
    def testcase_passwd_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "修改密码失败-密保错误"
        data = {
        "username":local_config.Username,
        "password":local_config.Passwd,
        "message":"1"
            }
        res = ApiDefine().Change_Passwd(self.session,data)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('用户或密保参数错误！',a)
        self.assertEqual(2004,b)


    @unittest.skip
    def testcase_passwd_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "修改密码失败-用户名为空"
        data = {
        "username":'',
        "password":local_config.Passwd,
        "message":"安般"
            }
        res = ApiDefine().Change_Passwd(self.session,data)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('username参数内容为空',a)
        self.assertEqual(2001,b)


    @unittest.skip
    def testcase_passwd_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "修改密码失败-密码为空"
        data = {
        "username":local_config.Username,
        "password":'',
        "message":"安般"
            }
        res = ApiDefine().Change_Passwd(self.session,data)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('password参数内容为空',a)
        self.assertEqual(2001,b)

    @unittest.skip
    def testcase_passwd_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "修改密码失败-密保为空"
        data = {
        "username":local_config.Username,
        "password":local_config.Passwd,
        "message":''
            }
        res = ApiDefine().Change_Passwd(self.session,data)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('用户或密保参数错误！',a)
        self.assertEqual(2004,b)

