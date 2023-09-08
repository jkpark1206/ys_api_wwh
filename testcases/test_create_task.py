import json
from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
import unittest
from common.Random_str import Ran_str
from common.Get_token import Token

class Create_Task_Test(Session_init):

    # @unittest.skip
    def test_creat_task_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "全选插件上传固件任务"
        token = ApiDefine().Get_token(self.session)
        task_name = '全选插件创建任务'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.all_have_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_task_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "全选插件关联固件库"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = '全选插件关联固件库'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,Ran_str(1),Ran_str(1),
                                        local_config.Plugin_All,file_md5,"true", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_task_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "创建任务失败—任务名为空"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务失败—任务名为空'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session,task_name,'',Ran_str(1),Ran_str(1),
                                        local_config.Plugin_All,file_md5,"true", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少task_name 参数", a)
        self.assertEqual(2001, b)



    # @unittest.skip
    def test_creat_task_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "创建任务失败—厂商为空"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务失败—版本号为空'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session,task_name,task_name,'',Ran_str(1),
                                    local_config.Plugin_All,file_md5,"true", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少vendor 参数", a)
        self.assertEqual(2001, b)



    # @unittest.skip
    def test_creat_task_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "创建任务失败—版本号为空"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务失败—版本号为空'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), '',
                                  local_config.Plugin_All, file_md5, "true", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少version 参数", a)
        self.assertEqual(2001, b)



    # @unittest.skip
    def test_creat_task_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "创建任务失败—device_name为空"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务失败—device_name为空'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session, '', task_name, Ran_str(1), Ran_str(1),
                                  local_config.Plugin_All, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少device_name 参数", a)
        self.assertEqual(2001, b)



    # @unittest.skip
    def test_creat_task_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "创建任务成功—任务名、版本、厂商为单个数字"
        token = ApiDefine().Get_token(self.session)
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session,1,1,1,1,
                                        local_config.Plugin_All,file_md5,"false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)


    # @unittest.skip
    def test_creat_task_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "创建任务成功—任务名、版本、厂商为单个字母"
        token = ApiDefine().Get_token(self.session)
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session,'a','a','a','a',
                                        local_config.Plugin_All,file_md5,"false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.skip
    def test_creat_task_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "创建任务成功—任务名、版本、厂商为单个特殊符号"
        token = ApiDefine().Get_token(self.session)
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  #根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session,'*','*','*','*',
                                        local_config.Plugin_All,file_md5,"false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.skip
    def test_creat_task_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = "创建任务成功—任务名、版本、厂商为99个字符"
        file_md5 = Get_file_md5(os.path.join(local_config.maxstr_task_path))  # 根据固件路径获取md5值
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, Ran_str(99), Ran_str(99), Ran_str(99), Ran_str(99),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.maxstr_task_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.skip
    def test_creat_task_11(self):
        self._testMethodName = 'case_11'
        self._testMethodDoc = "创建任务失败—任务名为100个字符"
        task_name = '创建任务—任务名为100个字符'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  # 根据固件路径获取md5值
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, Ran_str(100), Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("task_name参数长度超过100限制", a)
        self.assertEqual(2002, b)



    # @unittest.skip
    def test_creat_task_12(self):
        self._testMethodName = 'case_12'
        self._testMethodDoc = "创建任务失败—版本名为100个字符"
        task_name = '创建任务—版本名为100个字符'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  # 根据固件路径获取md5值
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(100),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("version参数长度超过100限制", a)
        self.assertEqual(2002, b)


    # @unittest.skip
    def test_creat_task_13(self):
        self._testMethodName = 'case_13'
        self._testMethodDoc = "创建任务失败—厂商名为100个字符"
        task_name = '创建任务—厂商名为100个字符'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  # 根据固件路径获取md5值
        h = {"Authorization": Token()}
        res =  ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(100), Ran_str(1),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("vendor参数长度超过100限制", a)
        self.assertEqual(2002, b)



    # @unittest.skip
    def test_creat_task_14(self):
        self._testMethodName = 'case_14'
        self._testMethodDoc = "创建任务失败—device_name为100个字符"
        task_name = '创建任务—device_name为100个字符'
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  # 根据固件路径获取md5值
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, Ran_str(100), task_name, Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("device_name参数长度超过100限制", a)
        self.assertEqual(2002, b)



    # @unittest.skip
    def test_creat_task_15(self):
        self._testMethodName = 'case_15'
        self._testMethodDoc = "创建任务失败—上传固件超过99个字符"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务—上传固件超过99个字符'
        file_md5 = Get_file_md5(os.path.join(local_config.overstr_task_path))  # 根据固件路径获取md5值
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, file_md5, "false", h, local_config.overstr_task_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("任务文件名超出最大长度:99", a)
        self.assertEqual(2005, b)


    # @unittest.skip
    def test_creat_task_16(self):
        self._testMethodName = 'case_16'
        self._testMethodDoc = "创建任务失败—MD5值为空"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务—MD5值为空'
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, '', "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("file_md5参数内容为空", a)
        self.assertEqual(2001, b)



    # @unittest.skip
    def test_creat_task_17(self):
        self._testMethodName = 'case_17'
        self._testMethodDoc = "创建任务失败—MD5值错误"
        token = ApiDefine().Get_token(self.session)
        task_name = '创建任务—MD5值错误'
        h = {"Authorization": token}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, 123, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("file_md5参数内容不符合要求", a)
        self.assertEqual(2005, b)



    # @unittest.skip
    def test_creat_task_18(self):
        self._testMethodName = 'case_18'
        self._testMethodDoc = "创建任务失败—MD5值与固件不符"
        task_name = '创建任务—MD5值与固件不符'
        firm_name = local_config.all_have_link_path.split('\\')[-1]
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        local_config.Plugin_All, 'ddc56d45ea7fc06a2684f589dadb4d29', "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("上传的固件{}不完整".format(firm_name), a)
        self.assertEqual(5004, b)



    # @unittest.skip
    def test_creat_task_19(self):
        self._testMethodName = 'case_19'
        self._testMethodDoc = "创建任务失败—重复勾选插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))  # 根据固件路径获取md5值
        task_name = '创建任务—重复勾选插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        '''["cwe_checker","cwe_checker"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("plugin参数里面有重复内容", a)
        self.assertEqual(2002, b)




    # @unittest.skip
    def test_creat_task_20(self):
        self._testMethodName = 'case_20'
        self._testMethodDoc = "创建任务失败—插件参数为空"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—插件参数为空'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        '', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("plugin参数格式错误", a)
        self.assertEqual(6002, b)



    # @unittest.skip
    def test_creat_task_21(self):
        self._testMethodName = 'case_21'
        self._testMethodDoc = "创建任务失败—不勾选插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                        '''[]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少 plugin 参数", a)
        self.assertEqual(6001, b)


    # @unittest.skip
    def test_creat_task_22(self):
        self._testMethodName = 'case_22'
        self._testMethodDoc = "创建任务失败—未上传固件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—未上传固件'
        h = {"Authorization": Token()}
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 1,
             "version": 1,
             "plugin": local_config.Plugin_All,
             "file_md5": file_md5}
        res = ApiDefine().Create_task(self.session, d, h, '')
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少固件", a)
        self.assertEqual(5001, b)



    # @unittest.skip
    def test_creat_task_23(self):
        self._testMethodName = 'case_23'
        self._testMethodDoc = "创建任务成功—只勾选cwe_checker插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选cwe_checker插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["cwe_checker"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)


    # @unittest.skip
    def test_creat_task_24(self):
        self._testMethodName = 'case_24'
        self._testMethodDoc = "创建任务成功—只勾选software_components插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选software_components插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["software_components"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_25(self):
        self._testMethodName = 'case_25'
        self._testMethodDoc = "创建任务成功—只勾选cve_lookup插件-关联software_components插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选cve_lookup插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["cve_lookup","software_components"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_26(self):
        self._testMethodName = 'case_26'
        self._testMethodDoc = "创建任务失败—只勾选cve_lookup插件-不关联software_components插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选cve_lookup插件-不关联software_components插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["cve_lookup"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("插件cve_lookup缺少依赖software_components", a)
        self.assertEqual(2002, b)



    # @unittest.skip
    def test_creat_task_27(self):
        self._testMethodName = 'case_27'
        self._testMethodDoc = "创建任务成功—只勾选crypto_hints插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选crypto_hints插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["crypto_hints"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.skip
    def test_creat_task_28(self):
        self._testMethodName = 'case_28'
        self._testMethodDoc = "创建任务成功—只勾选elf_analysis插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选elf_analysis插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["elf_analysis"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_29(self):
        self._testMethodName = 'case_29'
        self._testMethodDoc = "创建任务成功—只勾选sensitive_msg插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选sensitive_msg插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["sensitive_msg"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_30(self):
        self._testMethodName = 'case_30'
        self._testMethodDoc = "创建任务成功—只勾选elf_checksec插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—只勾选elf_checksec插件'
        h = {"Authorization": Token()}
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    '''["elf_checksec"]''', file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_32(self):
        self._testMethodName = 'case_32'
        self._testMethodDoc = "创建任务成功—不勾选elf_checksec插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选elf_checksec插件'
        h = {"Authorization": Token()}
        plugin='''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","sensitive_msg"]'''
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    plugin, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_33(self):
        self._testMethodName = 'case_33'
        self._testMethodDoc = "创建任务成功—不勾选sensitive_msg插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选users_and_passwords插件'
        h = {"Authorization": Token()}
        plugin ='''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","elf_checksec"]'''
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    plugin, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_35(self):
        self._testMethodName = 'case_35'
        self._testMethodDoc = "创建任务成功—不勾选elf_analysis插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选elf_analysis插件'
        h = {"Authorization": Token()}
        plugin = '''["cwe_checker","software_components","cve_lookup","crypto_hints","sensitive_msg","elf_checksec"]'''
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    plugin, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_36(self):
        self._testMethodName = 'case_36'
        self._testMethodDoc = "创建任务成功—不勾选crypto_hints插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选crypto_hints插件'
        h = {"Authorization": Token()}
        plugin = '''["cwe_checker","software_components","cve_lookup","elf_analysis","sensitive_msg","elf_checksec"]'''
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    plugin, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_37(self):
        self._testMethodName = 'case_37'
        self._testMethodDoc = "创建任务成功—不勾选cve_lookup插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选cve_lookup插件'
        h = {"Authorization": Token()}
        plugin='''["cwe_checker","software_components","crypto_hints","elf_analysis","sensitive_msg","elf_checksec"]'''
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    plugin, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)




    # @unittest.skip
    def test_creat_task_38(self):
        self._testMethodName = 'case_38'
        self._testMethodDoc = "创建任务成功—不勾选software_components插件"
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        task_name = '创建任务—不勾选software_components插件'
        h = {"Authorization": Token()}
        plugin = '''["cwe_checker","crypto_hints","elf_analysis","sensitive_msg","elf_checksec"]'''
        res = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                    plugin, file_md5, "false", h, local_config.all_have_link_path)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



