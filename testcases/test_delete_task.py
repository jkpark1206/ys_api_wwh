import json
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
from common.database_datas import OperationpostgresBase
import os

class Delete_task_test(Session_init):
    # @unittest.SkipTest
    def testcase_delete_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "成功删除单个任务（跳过固件库任务）"
        # 前提：创建一个未开始的固件库任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.initial_task_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'all',
             "version": 'all',
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": 'true'
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id_list":[task_id],
                    "skip_task_lib":True}
            res = ApiDefine().Delete_task(self.session, d2, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200, b)

    # @unittest.SkipTest
    def testcase_delete_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "成功删除多个任务（不跳过固件库任务）"
        # 前提：创建个未开始的固件任务
        task_id_2 = OperationpostgresBase().Sql_connect(0)
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.initial_task_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": 'false'
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id_1 = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id_list": [task_id_2,task_id_1],
                  "skip_task_lib": False}
            res = ApiDefine().Delete_task(self.session, d2, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            c = json.loads(res)["data"]["success"]
            self.assertIn("OK", a)
            self.assertEqual(200, b)
            self.assertIn("删除固件扫描任务:{}成功！".format(task_name), c[1]) #c[1]说明其中有两个任务，删除了两个任务

    # @unittest.SkipTest
    def testcase_delete_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "删除失败，删除不存在的任务"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_id = 1000000000000
        d = {"task_id_list":[task_id],
            "skip_task_lib": True}
        res = ApiDefine().Delete_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["fail"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)
        self.assertIn("扫描任务id:{}不存在".format(task_id), c)

    # @unittest.SkipTest
    def testcase_delete_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "删除失败，task_id_list为空"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {"task_id_list":[],
            "skip_task_lib": True}
        res = ApiDefine().Delete_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少task_id_list参数", a)
        self.assertEqual(2001, b)

    # @unittest.SkipTest
    def testcase_delete_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "删除失败，task_id_list不为列表格式"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {"task_id_list":1,
            "skip_task_lib": True}
        res = ApiDefine().Delete_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("参数类型错误！", a)
        self.assertEqual(2002, b)

    # @unittest.SkipTest
    def testcase_delete_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "删除失败，删除队列中的任务"
        # 前提：创建一个处于队列中的固件任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.initial_task_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": 'false'
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            ApiDefine().Start_task(self.session,d2,h)
            d3 = {"task_id_list": [task_id],
                  "skip_task_lib": False}
            res = ApiDefine().Delete_task(self.session, d3, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            c = json.loads(res)["data"]["fail"][0]
            self.assertIn("OK", a)
            self.assertEqual(200, b)
            self.assertIn('扫描任务:{}处于队列中,不可删除'.format(task_name),c)

    # @unittest.SkipTest
    def testcase_delete_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "删除失败，删除运行中的任务"
        # 前提：创建一个处于运行中的固件任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.all_have_link_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": 'false'
             }
        with open(local_config.all_have_link_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            ApiDefine().Start_task(self.session,d2,h)
            task_id_running = OperationpostgresBase().Sql_connect(2)
            print()
            d3 = {"task_id_list": [task_id_running],
                  "skip_task_lib": False}
            res = ApiDefine().Delete_task(self.session, d3, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            c = json.loads(res)["data"]["fail"][0]
            self.assertIn("OK", a)
            self.assertEqual(200, b)
            self.assertIn('处于运行中,不可删除'.format(task_name),c)


    # @unittest.SkipTest
    def testcase_delete_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "成功删除暂停中的任务"
        # 前提：创建一个处于暂停中的固件任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.all_have_link_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": 'false'
             }
        with open(local_config.all_have_link_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            ApiDefine().Start_task(self.session,d2,h)   #开始该任务
            ApiDefine().Stop_task(self.session,d2,h)    #暂停该任务
            d3 = {"task_id_list": [task_id],
                  "skip_task_lib": False}
            res = ApiDefine().Delete_task(self.session, d3, h)    #删除该任务
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            c = json.loads(res)["data"]["success"][0]
            self.assertIn("OK", a)
            self.assertEqual(200, b)
            self.assertIn('删除固件扫描任务'.format(task_name),c)

    # @unittest.SkipTest
    def testcase_delete_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "成功删除不可用的任务"
        # 前提：创建一个不可用的固件任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.unavailable_task_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.unavailable_task_path))
        d = {
            "device_name": task_name,
            "task_name": task_name,
            "vendor": task_name,
            "version": task_name,
            "plugin": local_config.Plugin_Cwe0,
            "file_md5": file_md5,
            "task_lib_tag": "false"  # true关联固件库
        }
        with open(local_config.unavailable_task_path,'rb') as firm:
            f = {'firmware': firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            ApiDefine().Start_task(self.session,d2,h)   #开始该任务
            task_id_unavailable = OperationpostgresBase().Sql_connect(4)
            d3 = {"task_id_list": [task_id_unavailable],
                "skip_task_lib": False}
            res = ApiDefine().Delete_task(self.session, d3, h)    #删除该任务
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            c = json.loads(res)["data"]["success"][0]
            self.assertIn("OK", a)
            self.assertEqual(200, b)
            self.assertIn('删除固件扫描任务'.format(task_name),c)



