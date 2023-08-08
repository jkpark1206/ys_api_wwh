import json
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine
import time
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
from common.database_datas import OperationpostgresBase

class Start_Task_Test(Session_init):

    # @unittest.SkipTest
    def test_start_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "开始初始状态的固件任务"
        #前提：创建一个未开始的任务
        token = ApiDefine().Get_token(self.session)
        task_name = '创建一个未开始的任务'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        h = {"Authorization": token}
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'all',
             "version": 'all',
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware":firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id":task_id}
            res = ApiDefine().Start_task(self.session, d2, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("OK", a)
            self.assertEqual(200, b)


    # @unittest.SkipTest
    def test_start_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "开始队列中的固件任务"
        token = ApiDefine().Get_token(self.session)
        task_id = OperationpostgresBase().Sql_connect(1)
        h = {"Authorization": token}
        d = {"task_id": task_id}
        res = ApiDefine().Start_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象处于队列中！！", a)
        self.assertEqual(3004, b)

    # @unittest.SkipTest
    def test_start_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "开始运行中的固件任务"
        token = ApiDefine().Get_token(self.session)
        task_id = OperationpostgresBase().Sql_connect(2)
        h = {"Authorization": token}
        d = {"task_id": task_id}
        res = ApiDefine().Start_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象正在运行！！", a)
        self.assertEqual(3005, b)

    # @unittest.SkipTest
    def test_start_04(self):
        self._testMethodName = 'case_04_1'
        self._testMethodDoc = "开始暂停状态的任务"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = '创建并开始一个新任务'
        file_md5 = Get_file_md5(os.path.join(local_config.stop_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'all',
             "version": 'all',
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
                 }
        with open(local_config.stop_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)
            task_id_stop = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id_stop}
            ApiDefine().Start_task(self.session, d2, h)
            #任务开始后，暂停任务
            ApiDefine().Stop_task(self.session, d2, h)
            res = ApiDefine().Start_task(self.session, d2, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("查询任务对象已停止！！", a)
            self.assertEqual(3011, b)


    # @unittest.SkipTest
    def test_start_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "开始已结束的固件任务"
        token = ApiDefine().Get_token(self.session)
        task_id = OperationpostgresBase().Sql_connect(3)
        h = {"Authorization": token}
        d = {"task_id": task_id}
        res = ApiDefine().Start_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象已结束！！", a)
        self.assertEqual(3006, b)

    # @unittest.SkipTest
    def test_start_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "开始不可用的固件任务"
        #前提：创建一个不可用的任务
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        task_name = '创建一个不可用的任务'
        #传入固件路径，获取不可用固件的md5
        file_md5 = Get_file_md5(os.path.join(local_config.unavailable_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'all',
             "version": 'all',
             "plugin": '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]''',
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        #输入固件路径，上传固件
        with open(local_config.unavailable_task_path,'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)
            task_id_ini = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id_ini}
            ApiDefine().Start_task(self.session, d2, h)
            task_id = OperationpostgresBase().Sql_connect(4)
            d = {"task_id": task_id}
            res = ApiDefine().Start_task(self.session, d, h)
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            self.assertIn("查询任务对象不支持解包！！", a)
            self.assertEqual(3006, b)

    # @unittest.SkipTest
    def test_start_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "开始任务失败-固件任务id不存在"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {"task_id":111111111111111111111111111111}
        res = ApiDefine().Start_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象不存在", a)
        self.assertEqual(3001, b)

#     # @unittest.SkipTest
    def test_start_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "开始任务失败-任务id为空"
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {"task_id": ''}
        res = ApiDefine().Start_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("参数类型错误！", a)
        self.assertEqual(2002, b)
