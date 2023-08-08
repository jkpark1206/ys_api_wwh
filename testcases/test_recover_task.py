import json
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
from common.database_datas import OperationpostgresBase

class Recover_Task_Test(Session_init):
    # @unittest.SkipTest
    def test_recover_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "恢复任务失败-恢复初始状态的固件任务"
        # 前提：创建一个未开始的任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = 'zsy.zip'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            res = ApiDefine().Recover_task(self.session, d2 , h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("未开始不可恢复任务", a)
            self.assertEqual(4013, b)

    # @unittest.SkipTest
    def test_recover_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "恢复任务失败-恢复队列中的固件任务"
        # 前提：创建一个未开始的任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = 'zsy.zip'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}   #获取该任务id
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
            res = ApiDefine().Recover_task(self.session, d2 , h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("固件扫描任务:zsy.zip处于队列中,不可恢复任务", a)
            self.assertEqual(4016, b)


    # @unittest.SkipTest
    def test_recover_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "恢复任务失败-恢复运行中的固件任务"
        # 前提：创建一个未开始的任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = 'zsy.zip'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}   #获取该任务id
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
            id_running = OperationpostgresBase().Sql_connect(2)   #获取运行中的任务，若没有，则获取队列中的任务，强制等待一分钟
            d_running = {"task_id": id_running}
            res = ApiDefine().Recover_task(self.session, d_running , h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("处于运行中,不可恢复任务", a)
            self.assertEqual(4017, b)


    # @unittest.SkipTest
    def test_recover_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "恢复任务成功-恢复暂停中的固件任务"
        # 前提：创建一个未开始的任务
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
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}   #获取该任务id
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
            ApiDefine().Stop_task(self.session, d2, h)    #暂停该任务
            res = ApiDefine().Recover_task(self.session, d2 , h)   #恢复该任务
            a = json.loads(res)["data"]
            b = json.loads(res)["code"]
            self.assertIn("恢复成功", a)
            self.assertEqual(200, b)

    # @unittest.SkipTest
    def test_recover_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "恢复任务失败-恢复已完成的固件任务"
        # 前提：创建一个未开始的任务
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
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}   #获取该任务id
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
            id_finished = OperationpostgresBase().Sql_connect(3)
            d3 = {"task_id": id_finished}
            res = ApiDefine().Recover_task(self.session, d3 , h)   #恢复该任务
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("已完成不可恢复任务", a)
            self.assertEqual(4015, b)


    # @unittest.SkipTest
    def test_recover_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "恢复任务失败-恢复不可用的固件任务"
        # 前提：创建一个不可用的任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = local_config.unavailable_task_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.unavailable_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.unavailable_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}   #获取该任务id
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
            id_finished = OperationpostgresBase().Sql_connect(4)
            d3 = {"task_id": id_finished}
            res = ApiDefine().Recover_task(self.session, d3 , h)   #恢复该任务
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("不支持解包不可恢复任务", a)
            self.assertEqual(4014, b)
