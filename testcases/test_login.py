from common.session_init import Session_init
import unittest
from common.api_demo import ApiDefine
from config.config import local_config
import json

class Login_Test(Session_init):

    @unittest.SkipTest
    def testcase_login_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "成功登录"
        res = ApiDefine().Login(self.session,local_config.Username,local_config.Passwd,local_config.Anban_Passwd)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)

    @unittest.skip
    def testcase_login_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "登录失败-用户名错误"
        res = ApiDefine().Login(self.session,111111,local_config.Passwd,local_config.Anban_Passwd)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("用户[111111]登录失败，原因：用户名或密码错误", a)
        self.assertEqual(2008, b)

    @unittest.skip
    def testcase_login_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "登录失败-密码错误"
        res = ApiDefine().Login(self.session,local_config.Username,111,111)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("用户[{}]登录失败，原因：用户名或密码错误".format(local_config.Username), a)
        self.assertEqual(2008, b)


    @unittest.skip
    def testcase_login_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "登录失败-用户名为空"
        res = ApiDefine().Login(self.session,'',local_config.Passwd,local_config.Anban_Passwd)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("username参数内容为空", a)
        self.assertEqual(2001, b)


    @unittest.skip
    def testcase_login_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "登录失败-密码为空"
        res = ApiDefine().Login(self.session,local_config.Username,'',local_config.Anban_Passwd)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("password参数内容为空", a)
        self.assertEqual(2001, b)

