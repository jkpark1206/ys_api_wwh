import unittest
from common.Md5_data import Get_file_md5
import json
from config.config import local_config
from common.api_demo import ApiDefine
from common.session_init import Session_init
from common.database_datas import OperationpostgresBase
import os


class Compare_task_test(Session_init):

    # @unittest.skip
    def test_compare_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功创建对比分析任务'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        f_id = OperationpostgresBase().Finished_task()[0][0]
        s_id = OperationpostgresBase().Finished_task()[1][0]
        d = {
            "first_id":f_id,
            "second_id":s_id
        }
        res = ApiDefine().Compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('OK',a)
        self.assertEqual(200, b)


    # @unittest.skip
    def test_compare_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = '创建对比分析任务失败-first_id为空'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        s_id = OperationpostgresBase().Finished_task()[1][0]
        d = {
            "first_id":'',
            "second_id":s_id
        }
        res = ApiDefine().Compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('参数类型错误！',a)
        self.assertEqual(2002, b)

    # @unittest.skip
    def test_compare_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = '创建对比分析任务失败-second_id为空'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        f_id = OperationpostgresBase().Finished_task()[0][0]
        d = {
            "first_id":f_id,
            "second_id":''
        }
        res = ApiDefine().Compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('参数类型错误！',a)
        self.assertEqual(2002, b)

    # @unittest.skip
    def test_compare_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = '创建对比分析任务失败-任务id相同'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {
            "first_id":1,
            "second_id":1
        }
        res = ApiDefine().Compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('对比任务id相同',a)
        self.assertEqual(2003, b)


    # @unittest.skip
    def test_compare_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = '创建对比分析任务失败-存在运行中任务id'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        f_id = OperationpostgresBase().Finished_task()[0][0]
        task_name = '暂停运行中的固件任务'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe/user/elf0',
             "version": 'cwe/user/elf0',
             "plugin": local_config.Plugin_Cwe0,
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
        s_id = OperationpostgresBase().Sql_connect(2)
        d = {
            "first_id":f_id,
            "second_id":s_id
        }
        res = ApiDefine().Compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('任务正在运行, 无法比较!',a)
        self.assertEqual(3005, b)


    # @unittest.skip
    def test_compare_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = '创建对比分析任务失败-存在暂停中任务id'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        f_id = OperationpostgresBase().Finished_task()[0][0]
        task_name = '暂停运行中的固件任务'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe/user/elf0',
             "version": 'cwe/user/elf0',
             "plugin": local_config.Plugin_Cwe0,
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
            id2 = OperationpostgresBase().Sql_connect(2)
            d3 = {"task_id": id2}
            ApiDefine().Stop_task(self.session, d3, h)  # 暂停运行中的任务
        s_id = OperationpostgresBase().Sql_connect(5)
        d = {
            "first_id":f_id,
            "second_id":s_id
        }
        res = ApiDefine().Compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('任务正在运行, 无法比较!',a)
        self.assertEqual(3005, b)


    # @unittest.skip
    def test_compare_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = '创建对比分析任务失败-存在未开始任务id'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        f_id = OperationpostgresBase().Finished_task()[0][0]
        task_name = 'zsy.zip'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": local_config.Plugin_Cwe0,
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.initial_task_path, 'rb') as firm:
            f = {"firmware": firm}
            ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务
        s_id = OperationpostgresBase().Sql_connect(0)
        d = {
            "first_id": f_id,
            "second_id": s_id
        }
        res = ApiDefine().Compare_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('任务正在运行, 无法比较!', a)
        self.assertEqual(3005, b)


    # @unittest.skip
    def test_compare_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = '创建对比分析任务失败-存在不可用任务id'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        f_id = OperationpostgresBase().Finished_task()[0][0]
        task_name = local_config.unavailable_task_path.split('\\')[-1]
        file_md5 = Get_file_md5(os.path.join(local_config.unavailable_task_path))
        d = {"device_name": task_name,
             "task_name": task_name,
             "vendor": 'cwe0',
             "version": 'cwe0',
             "plugin": local_config.Plugin_Cwe0,
             "file_md5": file_md5,
             "task_lib_tag": "false"
             }
        with open(local_config.unavailable_task_path, 'rb') as firm:
            f = {"firmware": firm}
            res_ini = ApiDefine().Create_task(self.session, d, h, f)  # 先创建一个任务，获取任务task_id
            task_id = json.loads(res_ini)["data"]["id"]
            d2 = {"task_id": task_id}  # 获取该任务id
            ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
        s_id = OperationpostgresBase().Sql_connect(4)
        d = {
            "first_id": f_id,
            "second_id": s_id
        }
        res = ApiDefine().Compare_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('任务不可用, 无法比较!', a)
        self.assertEqual(3009, b)
