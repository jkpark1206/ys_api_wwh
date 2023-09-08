import json
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine
from common.Get_token import Token
from common.Random_str import Ran_str
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
from common.database_datas import OperationpostgresBase


class Stop_Task_Test(Session_init):
    # @unittest.SkipTest
    def test_stop_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "暂停初始状态的固件任务"
        #前提：创建一个未开始的任务
        h = {"Authorization": Token()}
        task_name = 'zsy.zip'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        res_ini = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                            local_config.Plugin_Cwe0, file_md5, 'false', h,
                                            local_config.initial_task_path)  #先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        d2 = {"task_id": task_id}
        res = ApiDefine().Stop_task(self.session, d2, h)  #暂停未开始的任务
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("固件扫描任务:{}未开始不可停止任务".format(task_name), a)
        self.assertEqual(4009, b)



    # @unittest.SkipTest
    def test_stop_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "成功暂停队列中的固件任务"
        #前提：创建一个未开始的任务
        h = {"Authorization": Token()}
        task_name = '暂停队列中的固件任务'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        res_ini = ApiDefine().Create_task_2(self.session, task_name, task_name, Ran_str(1), Ran_str(1),
                                            local_config.Plugin_Cwe0, file_md5, 'false', h,
                                            local_config.initial_task_path)  #先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        d2 = {"task_id": task_id}
        ApiDefine().Start_task(self.session, d2, h)   #开始该任务
        res = ApiDefine().Stop_task(self.session, d2, h)  #暂停已开始的任务
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.SkipTest
    def test_stop_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "成功暂停运行中的固件任务"
        # 前提：创建一个未开始的任务
        h = {"Authorization": Token()}
        task_name = '暂停运行中的固件任务'
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        res_ini = ApiDefine().Create_task_2(self.session,task_name,task_name,Ran_str(1),Ran_str(1),
                                            local_config.Plugin_Cwe0,file_md5,'false',h,
                                            local_config.initial_task_path)  # 先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        d2 = {"task_id": task_id}
        ApiDefine().Start_task(self.session, d2, h)  # 开始该任务
        id2 = OperationpostgresBase().Sql_connect(2)
        d3 = {"task_id": id2}
        res = ApiDefine().Stop_task(self.session, d3, h)  # 暂停运行中的任务
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.SkipTest
    def test_stop_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "暂停已暂停的固件任务"
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Sql_connect(5)
        d = {"task_id" : task_id}
        res = ApiDefine().Stop_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("任务已停止,无需再次停止任务", a)
        self.assertEqual(4011, b)


    # @unittest.SkipTest
    def test_stop_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "暂停已完成的固件任务"
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Sql_connect(3)
        d = {"task_id" : task_id}
        res = ApiDefine().Stop_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("已完成不可停止任务", a)
        self.assertEqual(4012, b)


    # @unittest.SkipTest
    def test_stop_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "暂停失败-任务id不存在"
        h = {"Authorization": Token()}
        d = {"task_id" : 1111111111111111111111111111111111111111}
        res = ApiDefine().Stop_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("固件扫描任务id:1111111111111111111111111111111111111111不存在", a)
        self.assertEqual(3001, b)



    # @unittest.SkipTest
    def test_stop_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "暂停失败-任务id不可为空"
        h = {"Authorization": Token()}
        d = {"task_id" : ''}
        res = ApiDefine().Stop_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("参数类型错误！", a)
        self.assertEqual(2002, b)