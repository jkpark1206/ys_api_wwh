import json
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine
from common.Get_token import Token
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
from common.database_datas import OperationpostgresBase

class Start_Task_Test(Session_init):

    @unittest.SkipTest
    def test_start_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "开始初始状态的固件任务"
        #前提：创建一个未开始的任务
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_all)
        h = {"Authorization": Token()}
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.initial_task_path)
        task_id = json.loads(res_ini)["data"]["id"]
        res = ApiDefine().Start_task(self.session, h, task_id)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)


    @unittest.SkipTest
    def test_start_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "开始队列中的固件任务"
        task_id = OperationpostgresBase().Sql_connect(1)
        h = {"Authorization": Token()}
        d = {"task_id": task_id}
        res = ApiDefine().Start_task(self.session, d, h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象处于队列中！！", a)
        self.assertEqual(3004, b)



    @unittest.SkipTest
    def test_start_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "开始运行中的固件任务"
        task_id = OperationpostgresBase().Sql_connect(2)
        h = {"Authorization": Token()}
        res = ApiDefine().Start_task(self.session, h, task_id)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象正在运行！！", a)
        self.assertEqual(3005, b)


    @unittest.SkipTest
    def test_start_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "开始暂停状态的任务"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_all)
        file_md5 = Get_file_md5(os.path.join(local_config.stop_task_path))
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.stop_task_path)
        task_id_stop = json.loads(res_ini)["data"]["id"]
        # 任务开始后
        ApiDefine().Start_task(self.session, h, task_id_stop)
        #暂停任务
        ApiDefine().Stop_task(self.session, h, task_id_stop)
        # 开始已暂停的任务
        res = ApiDefine().Start_task(self.session, h, task_id_stop)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象已停止！！", a)
        self.assertEqual(3011, b)


    @unittest.SkipTest
    def test_start_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "开始已结束的固件任务"
        task_id = OperationpostgresBase().Sql_connect(3)
        h = {"Authorization": Token()}
        res = ApiDefine().Start_task(self.session, h, task_id)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象已结束！！", a)
        self.assertEqual(3006, b)


    @unittest.SkipTest
    def test_start_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "开始不可用的固件任务"
        #前提：创建一个不可用的任务
        h = {"Authorization": Token()}
        #创建一个不可用的任务
        file_md5 = Get_file_md5(os.path.join(local_config.unavailable_task_path))
        s_id = OperationpostgresBase().Get_initial_strategy()
        #输入固件路径，上传固件
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.unavailable_task_path)
        task_id_ini = json.loads(res_ini)["data"]["id"]
        ApiDefine().Start_task(self.session, h, task_id_ini)
        task_id = OperationpostgresBase().Sql_connect(4)
        res = ApiDefine().Start_task(self.session, h, task_id)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象不支持解包！！", a)
        self.assertEqual(3006, b)


    @unittest.SkipTest
    def test_start_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "开始任务失败-固件任务id不存在"
        h = {"Authorization": Token()}
        res = ApiDefine().Start_task(self.session, h, 111111111111111111111111111111)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("查询任务对象不存在", a)
        self.assertEqual(3001, b)


    @unittest.SkipTest
    def test_start_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "开始任务失败-任务id为空"
        h = {"Authorization": Token()}
        res = ApiDefine().Start_task(self.session, h, '')
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("参数类型错误！", a)
        self.assertEqual(2002, b)


