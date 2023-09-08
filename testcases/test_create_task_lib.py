import json
import unittest
from common.Random_str import Ran_str
from common.api_demo import ApiDefine
from common.session_init import Session_init
from common.Md5_data import Get_file_md5
from config.config import local_config
import os

class Create_task_lib(Session_init):

    @unittest.skip
    def test_create_task_lib_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功创建固件库任务'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        d = {"device_name":1,
             "task_name":1,
             "vendor": 1,
             "version": 1,
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('OK',a)
                self.assertEqual(200, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = '创建固件库任务失败-插件勾选不完全'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        d = {"device_name":1,
             "task_name":1,
             "vendor": 'all',
             "version": 'all',
             "plugin":local_config.Plugin_Cwe0,
             "file_md5": md_5,
             "task_lib_tag":"false"}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整',a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = '创建固件库任务成功-任务名称、厂商、版本为单个字母'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        d = {"device_name":'a',
             "task_name":'a',
             "vendor": 'a',
             "version": 'a',
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('OK',a)
                self.assertEqual(200, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = '创建固件库任务成功-任务名称、厂商、版本为单个特殊符号'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        d = {"device_name":'*',
             "task_name":'*',
             "vendor": '*',
             "version": '*',
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('OK',a)
                self.assertEqual(200, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = '创建固件库任务成功-任务名称、厂商、版本为99个字符'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str = Ran_str(99)
        d = {"device_name":rand_str,
             "task_name":rand_str,
             "vendor": rand_str,
             "version": rand_str,
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('OK',a)
                self.assertEqual(200, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = '创建固件库任务成功-任务名称、厂商、版本为99个字符'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str = Ran_str(99)
        d = {"device_name":rand_str,
             "task_name":rand_str,
             "vendor": rand_str,
             "version": rand_str,
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('OK',a)
                self.assertEqual(200, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = '创建固件库任务失败-任务名称为100个字符'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        rand_str_100 = Ran_str(100)
        d = {"device_name":rand_str_1,
             "task_name":rand_str_100,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('task_name参数长度超过100限制',a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = '创建固件库任务失败-厂商为100个字符'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        rand_str_100 = Ran_str(100)
        d = {"device_name":rand_str_1,
             "task_name":rand_str_1,
             "vendor": rand_str_100,
             "version": rand_str_1,
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('vendor参数长度超过100限制',a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = '创建固件库任务失败-版本为100个字符'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization':token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        rand_str_100 = Ran_str(100)
        d = {"device_name":rand_str_1,
             "task_name":rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_100,
             "plugin":local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path,'rb') as firm:
            f = {'firmware':firm}
            res = ApiDefine().Create_task_lib(self.session,d,h,f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('version参数长度超过100限制',a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = '创建固件库任务失败-device_name为100个字符'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        rand_str_100 = Ran_str(100)
        d = {"device_name": rand_str_100,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('device_name参数长度超过100限制', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_11(self):
        self._testMethodName = 'case_11'
        self._testMethodDoc = '创建固件库任务失败-device_name为空'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        d = {"device_name": '',
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('缺少device_name 参数', a)
                self.assertEqual(2001, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_12(self):
        self._testMethodName = 'case_12'
        self._testMethodDoc = '创建固件库任务失败-任务名称为空'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": '',
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('缺少task_name 参数', a)
                self.assertEqual(2001, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_13(self):
        self._testMethodName = 'case_13'
        self._testMethodDoc = '创建固件库任务失败-厂商为空'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": '',
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('缺少vendor 参数', a)
                self.assertEqual(2001, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_14(self):
        self._testMethodName = 'case_14'
        self._testMethodDoc = '创建固件库任务失败-版本为空'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md_5 = Get_file_md5(os.path.join(local_config.all_have_path))
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": '',
             "plugin": local_config.Plugin_All,
             "file_md5": md_5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('缺少version 参数', a)
                self.assertEqual(2001, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_15(self):
        self._testMethodName = 'case_15'
        self._testMethodDoc = '创建固件库任务失败-md5值为空'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": ''}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('file_md5参数内容为空', a)
                self.assertEqual(2001, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_16(self):
        self._testMethodName = 'case_16'
        self._testMethodDoc = '创建固件库任务失败-上传文件为空'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_link_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": md5}
        f = {'firmware': ''}
        res = ApiDefine().Create_task_lib(self.session, d, h, f)
        try:
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn('上传的固件firmware不完整', a)
            self.assertEqual(5004, b)
        except Exception as e:
            print(e)



    @unittest.skip
    def test_create_task_lib_17(self):
        self._testMethodName = 'case_17'
        self._testMethodDoc = '创建固件库任务失败-md5值错误'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        rand_str_1 = Ran_str(1)
        firm_name = local_config.all_have_path.split('\\')[-1]
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_All,
             "file_md5": 'ddc56d45ea7fc06a2684f589dadb4d20'}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('上传的固件{}不完整'.format(firm_name), a)
                self.assertEqual(5004, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_18(self):
        self._testMethodName = 'case_18'
        self._testMethodDoc = '创建固件库任务失败-勾选插件重复'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('plugin参数里面有重复内容', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_19(self):
        self._testMethodName = 'case_19'
        self._testMethodDoc = '创建固件库任务失败-勾选插件名错误'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["ce_checker"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('plugin不正确或超出范围', a)
                self.assertEqual(6003, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_20(self):
        self._testMethodName = 'case_20'
        self._testMethodDoc = '创建固件库任务失败-不勾选插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''[]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('缺少 plugin 参数', a)
                self.assertEqual(6001, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_21(self):
        self._testMethodName = 'case_21'
        self._testMethodDoc = '创建固件库任务失败-不勾选cve插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": local_config.Plugin_Cve0,
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_22(self):
        self._testMethodName = 'case_22'
        self._testMethodDoc = '创建固件库任务失败-不勾选software_components及cve插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_23(self):
        self._testMethodName = 'case_23'
        self._testMethodDoc = '创建固件库任务失败-不勾选software_components但勾选cve插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件cve_lookup缺少依赖software_components', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_24(self):
        self._testMethodName = 'case_24'
        self._testMethodDoc = '创建固件库任务失败-不勾选crypto_hints插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","software_components","cve_lookup","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_25(self):
        self._testMethodName = 'case_25'
        self._testMethodDoc = '创建固件库任务失败-不勾选elf_analysis插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)


    @unittest.skip
    def test_create_task_lib_26(self):
        self._testMethodName = 'case_26'
        self._testMethodDoc = '创建固件库任务失败-不勾选ip_and_uri_finder插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","users_and_passwords","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_27(self):
        self._testMethodName = 'case_27'
        self._testMethodDoc = '创建固件库任务失败-不勾选users_and_passwords插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","elf_checksec"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)



    @unittest.skip
    def test_create_task_lib_28(self):
        self._testMethodName = 'case_28'
        self._testMethodDoc = '创建固件库任务失败-不勾选elf_checksec插件'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        md5 = Get_file_md5(local_config.all_have_path)
        rand_str_1 = Ran_str(1)
        d = {"device_name": rand_str_1,
             "task_name": rand_str_1,
             "vendor": rand_str_1,
             "version": rand_str_1,
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords"]''',
             "file_md5": md5}
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res = ApiDefine().Create_task_lib(self.session, d, h, f)
            try:
                a = json.loads(res)["message"]
                b = json.loads(res)["code"]
                self.assertIn('插件参数不完整', a)
                self.assertEqual(2002, b)
            except Exception as e:
                print(e)
