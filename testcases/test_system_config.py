import unittest
from common.Random_str import Ran_str
from common.session_init import Session_init
from config.config import local_config
from common.api_demo import ApiDefine
import json

class System_config(Session_init):

    # @unittest.skip
    def test_sys_conf_case_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功配置产品信息'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":"a",
            "version":"a"
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品信息配置成功",a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)

    # @unittest.skip
    def test_sys_conf_case_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = '配置产品信息失败-非config用户登录无配置权限'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        d = {
            "name": "易识",
            "version": "v2.10"
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f = {
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data=d, files=f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("用户无权限, 修改产品配置失败", a)
            self.assertEqual(1011, b)
        except Exception as e:
            print(e,res)


    # @unittest.skip
    def test_sys_conf_case_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = '配置产品信息成功-信息为最大边界值'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":Ran_str(20),
            "version":Ran_str(30)
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品信息配置成功",a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_sys_conf_case_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = '配置产品信息失败-产品名称超过20个字符'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":Ran_str(21),
            "version":1
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品名称参数长度错误,最大长度为20",a)
            self.assertEqual(2000,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_sys_conf_case_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = '配置产品信息失败-版本名超过30个字符'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":1,
            "version":Ran_str(31)
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品版本参数长度错误,最大长度为30",a)
            self.assertEqual(2000,b)
        except Exception as e:
            print(e)



    # @unittest.skip
    def test_sys_conf_case_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = '配置产品信息失败-PDF报告水印超过大小限制'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":Ran_str(5),
            "version":Ran_str(5)
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_png_over_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品信息配置失败, 文件大小超出限制",a)
            self.assertEqual(1011,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_sys_conf_case_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = '配置产品信息失败-正常logo超过大小限制'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":Ran_str(5),
            "version":Ran_str(5)
        }
        picture_logo = open(local_config.Logo_svg_over_path, "rb")
        text_logo = open(local_config.Logo_white_logo_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品信息配置失败, 文件大小超出限制",a)
            self.assertEqual(1011,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_sys_conf_case_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = '配置产品信息失败-白色logo超过大小限制'
        token = ApiDefine().Get_config_token(self.session)
        h = {'Authorization': token}
        d = {
            "name":Ran_str(5),
            "version":Ran_str(5)
        }
        picture_logo = open(local_config.Logo_normal_logo_path, "rb")
        text_logo = open(local_config.Logo_svg_over_path, "rb")
        browser_logo = open(local_config.Logo_web_logo_path, "rb")
        watermark_logo = open(local_config.Logo_watermark_logo_path, "rb")
        f={
            "picture_logo": picture_logo,
            "text_logo": text_logo,
            "browser_logo": browser_logo,
            "watermark_logo": watermark_logo
        }
        res = ApiDefine().System_config(self.session, headers=h, data = d, files = f)
        picture_logo.close()
        text_logo.close()
        browser_logo.close()
        watermark_logo.close()
        try:
            a = json.loads(res)['message']
            b = json.loads(res)['code']
            self.assertIn("产品信息配置失败, 文件大小超出限制",a)
            self.assertEqual(1011,b)
        except Exception as e:
            print(e)






