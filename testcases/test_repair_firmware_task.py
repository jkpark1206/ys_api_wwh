import json
import time

from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
import unittest
from common.Random_str import *
from common.Get_token import Token
from common.database_datas import OperationpostgresBase

class Repair_Firmware_Task_Test(Session_init):

    @unittest.skip
    def test_remise_create_task(self):
        # 前提：先创建一个任务
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        file_md5 = Get_file_md5(local_config.initial_task_path)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.initial_task_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn('OK', b)


    @unittest.skip
    def test_repair_task_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "修改成功-修改任务名称为单个字母/只勾选cwe"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_cwe)
        task_id = OperationpostgresBase().Sql_connect(0)
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(1))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200,a)
        self.assertIn('OK', b)

    @unittest.skip
    def test_repair_task_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "修改成功-修改任务名称为单个数字\只勾选soft插件"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_soft)
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Random_num())
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200,a)
        self.assertIn('OK', b)


    @unittest.skip
    def test_repair_task_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "修改成功-任务名称为100个字符\只勾选soft-cve插件"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_cve_soft)
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(100))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200,a)
        self.assertIn('OK', b)


    @unittest.skip
    def test_repair_task_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "修改失败-任务名称为101个字符"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(101))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2002,a)
        self.assertIn('任务名称参数超出范围', b)


    @unittest.skip
    def test_repair_task_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "修改失败-任务名称为空"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, '')
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2002,a)
        self.assertIn('任务名称参数超出范围', b)


    @unittest.skip
    def test_repair_task_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "修改失败-任务id为0"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        res = ApiDefine().Repair_Firmware_Task(self.session , h, 00, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2001,a)
        self.assertIn('扫描任务ID参数为空', b)


    @unittest.skip
    def test_repair_task_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "修改失败-任务id为空"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        res = ApiDefine().Repair_Firmware_Task(self.session , h, '', s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2002,a)
        self.assertIn('参数类型错误！', b)


    @unittest.skip
    def test_repair_task_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "修改失败-分析策略id不存在"
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, 0, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3001,a)
        self.assertIn('策略不存在', b)


    @unittest.skip
    def test_repair_task_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "修改失败-分析策略id为空"
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, '', Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2002,a)
        self.assertIn('参数类型错误！', b)


    @unittest.skip
    def test_repair_task_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = "修改失败-修改运行中的任务"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        task_id = OperationpostgresBase().Sql_connect(0)  #获取未开始的任务id
        ApiDefine().Start_task(self.session,h,task_id)  #开始任务
        task_id_2 = OperationpostgresBase().Sql_connect(2)
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id_2, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3005,a)
        self.assertIn('正在运行，不可修改！', b)


    @unittest.skip
    def test_repair_task_11(self):
        self._testMethodName = 'case_11'
        self._testMethodDoc = "修改失败-修改已完成的任务"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        task_id = OperationpostgresBase().Sql_connect(3)  #获取已结束的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3006,a)
        self.assertIn('已结束，不可修改！', b)


    @unittest.skip
    def test_repair_task_12(self):
        self._testMethodName = 'case_12'
        self._testMethodDoc = "修改失败-修改不可用的任务"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        res_running = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.unavailable_task_path)
        task_id = json.loads(res_running )["data"]["id"]
        ApiDefine().Start_task(self.session, h, task_id)
        task_id = OperationpostgresBase().Sql_connect(4)  #获取已结束的任务id
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3009,a)
        self.assertIn('不可用，不可修改！', b)



    @unittest.skip
    def test_repair_task_13(self):
        self._testMethodName = 'case_13'
        self._testMethodDoc = "修改失败-修改暂停中的任务"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        file_md5 = Get_file_md5(local_config.initial_task_path)
        ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.initial_task_path) #前提：创建任务
        task_id = OperationpostgresBase().Sql_connect(0)  # 获取未开始的任务id
        ApiDefine().Start_task(self.session, h, task_id)  # 开始任务
        task_id_2 = OperationpostgresBase().Sql_connect(2)  #获取运行中的任务
        ApiDefine().Stop_task(self.session,h,task_id_2)
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3011,a)
        self.assertIn('已暂停，不可修改！', b)


    @unittest.skip
    def test_repair_task_14(self):
        self._testMethodName = 'case_14'
        self._testMethodDoc = "修改失败-任务id不存在"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        res = ApiDefine().Repair_Firmware_Task(self.session , h, 10000, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3001,a)
        self.assertIn('查询任务对象不存在', b)


    @unittest.skip
    def test_repair_task_15(self):
        self._testMethodName = 'case_15'
        self._testMethodDoc = "修改成功-只勾选sensitive_msg插件"
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Sql_connect(0)
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_sensitive_msg)
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200,a)
        self.assertIn('OK', b)


    @unittest.skip
    def test_repair_task_16(self):
        self._testMethodName = 'case_16'
        self._testMethodDoc = "修改成功-只勾选security插件"
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Sql_connect(0)
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_security)
        res = ApiDefine().Repair_Firmware_Task(self.session , h, task_id, s_id, Ran_str(2))
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200,a)
        self.assertIn('OK', b)


