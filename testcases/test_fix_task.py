import json
from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
from common.Get_token import Token
import unittest
from common.Random_str import Ran_str

class Fix_Task_Test(Session_init):

    # @unittest.skip
    def test_Fix_task_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "修改任务不勾选cve插件"
        task_name = '修改任务不勾选cve插件'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,'all','all',local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertIs(200, b)
        except Exception as e:
            print(e)

    # @unittest.skip
    def test_Fix_task_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "修改任务不勾选插件"
        task_name = '修改任务不勾选插件'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,'all','all',local_config.Plugin0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("缺少 plugin 参数", a)
            self.assertEqual(6001,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "修改任务插件参数为空"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,'all','all','','false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("plugin参数格式错误", a)
            self.assertEqual(6002,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "修改任务插件未全选-关联固件库"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,'a','a',local_config.Plugin_Cve0,'true',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("当前所选插件不完整", a)
            self.assertEqual(6001,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "修改任务失败：task_name为100个字符"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,Ran_str(100),'a','a',local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("task_name参数长度超过100限制", a)
            self.assertEqual(2002,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "修改任务失败：vendor参数长度为100"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(100),'a',local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("vendor参数长度超过100限制", a)
            self.assertEqual(2002,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "修改任务失败：version为100个字符"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(100),local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("version参数长度超过100限制", a)
            self.assertEqual(2002,b)
        except Exception as e:
            print(e)

    # @unittest.skip
    def test_Fix_task_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "修改任务失败：task_name为空"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,'',Ran_str(1),Ran_str(1),local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("缺少task_name 参数", a)
            self.assertEqual(2001,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "修改任务失败：vendor为空"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,'',Ran_str(1),local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("缺少vendor 参数", a)
            self.assertEqual(2001,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = "修改任务失败：version为空"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,'',Ran_str(1),local_config.Plugin_Cve0,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("缺少vendor 参数", a)
            self.assertEqual(2001,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_11(self):
        self._testMethodName = 'case_11'
        self._testMethodDoc = "修改任务失败：plugin重复"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["cwe_checker","software_components","crypto_hints","cwe_checker"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("plugin参数里面有重复内容", a)
            self.assertEqual(2002,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_12(self):
        self._testMethodName = 'case_12'
        self._testMethodDoc = "修改任务失败：id为空"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        res_2 = ApiDefine().Fix_task(self.session, '', task_name, task_name, Ran_str(1), Ran_str(1), local_config.Plugin_Cve0, 'false', h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("参数类型错误！", a)
            self.assertEqual(2002, b)
        except Exception as e:
            print(e)



    # @unittest.skip
    def test_Fix_task_13(self):
        self._testMethodName = 'case_13'
        self._testMethodDoc = "修改任务失败：勾选cve插件/不勾选soft插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["cve_lookup"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("插件cve_lookup缺少依赖['software_components', 'homology']", a)
            self.assertEqual(2002,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_14(self):
        self._testMethodName = 'case_14'
        self._testMethodDoc = "修改任务失败：勾选cve插件/不勾选soft插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["cve_lookup"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("插件cve_lookup缺少依赖['software_components', 'homology']", a)
            self.assertEqual(2002,b)
        except Exception as e:
            print(e)

    # @unittest.skip
    def test_Fix_task_15(self):
        self._testMethodName = 'case_15'
        self._testMethodDoc = "修改任务成功：勾选cve插件-关联勾选soft插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["software_components","cve_lookup"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_16(self):
        self._testMethodName = 'case_16'
        self._testMethodDoc = "修改任务成功：99个字符，只勾选crypto_hints插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["crypto_hints"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,Ran_str(99),Ran_str(99),Ran_str(99),Ran_str(99),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)

    # @unittest.skip
    def test_Fix_task_17(self):
        self._testMethodName = 'case_17'
        self._testMethodDoc = "修改任务成功：只勾选elf_analysis插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["elf_analysis"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)

    # @unittest.skip
    def test_Fix_task_18(self):
        self._testMethodName = 'case_18'
        self._testMethodDoc = "修改任务成功：只勾选elf_checksec插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["elf_checksec"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_19(self):
        self._testMethodName = 'case_19'
        self._testMethodDoc = "修改任务成功：只勾选sensitive_msg插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["sensitive_msg"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,task_name,task_name,Ran_str(1),Ran_str(1),plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_Fix_task_20(self):
        self._testMethodName = 'case_20'
        self._testMethodDoc = "修改任务成功：单个特殊符号，只勾选software_components插件"
        task_name = '自动化测试'
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, local_config.all_have_path)
        id = json.loads(res)["data"]["id"]
        plugin = '''["software_components"]'''
        res_2 = ApiDefine().Fix_task(self.session,id,"*","*","*","*",plugin,'false',h)
        try:
            a = json.loads(res_2)["message"]
            b = json.loads(res_2)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200,b)
        except Exception as e:
            print(e)

