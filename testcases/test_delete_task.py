import json
import time
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine
from common.Get_token import Token
from common.Random_str import Ran_str
from config.config import local_config
from common.Md5_data import Get_file_md5
from common.database_datas import OperationpostgresBase
import os



class Delete_task_test(Session_init):

    @unittest.SkipTest
    def testcase_delete_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "成功删除单个任务（跳过固件库任务）"
        # 前提：创建一个未开始的固件库任务
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        s_id = OperationpostgresBase().lib_strategy_id()
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.initial_task_path)  # 先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        res = ApiDefine().Delete_task(self.session, h,[task_id],True)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    @unittest.SkipTest
    def testcase_delete_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "成功删除多个任务（不跳过固件库任务）"
        # 前提：创建个未开始的固件任务
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().lib_strategy_id()
        #前提：创建2个未开始的任务
        file_md5_1 = Get_file_md5(os.path.join(local_config.initial_task_path))
        res_ini_1 = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5_1, local_config.initial_task_path)  # 先创建一个任务，获取任务task_id
        task_id_1 = json.loads(res_ini_1)["data"]["id"]
        file_md5_2 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        res_ini_2 = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5_2,
                                                     local_config.all_have_link_path)  # 先创建一个任务，获取任务task_id
        task_id_2 = json.loads(res_ini_2)["data"]["id"]
        res = ApiDefine().Delete_task(self.session, h, [task_id_1,task_id_2],False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["success"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)
        self.assertIn("成功！", c[1]) #c[1]说明其中有两个任务，删除了两个任务

    @unittest.SkipTest
    def testcase_delete_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "删除失败，删除不存在的任务"
        h = {"Authorization": Token()}
        res = ApiDefine().Delete_task(self.session, h, [10000000], False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["fail"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)
        self.assertIn("扫描任务id:10000000不存在", c)


    @unittest.SkipTest
    def testcase_delete_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "删除失败，task_id_list为空"
        h = {"Authorization": Token()}
        res = ApiDefine().Delete_task(self.session, h, [], True)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("缺少task_id_list参数", a)
        self.assertEqual(2001, b)


    @unittest.SkipTest
    def testcase_delete_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "删除失败，task_id_list不为列表格式"
        h = {"Authorization": Token()}
        res = ApiDefine().Delete_task(self.session, h, 1, True)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("参数类型错误！", a)
        self.assertEqual(2002, b)


    @unittest.SkipTest
    def testcase_delete_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "删除失败，删除队列中的任务-需要创建7个任务-跳过"
        # 前提：创建一个处于队列中的固件任务
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        s_id = OperationpostgresBase().Get_initial_strategy()
        res_ini = ApiDefine().Create_Firmware_Task(self.session,h,s_id,file_md5,
                                            local_config.initial_task_path)  # 先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        ApiDefine().Start_task(self.session,h,task_id)
        res = ApiDefine().Delete_task(self.session, h,[task_id] ,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["fail"][0]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    @unittest.SkipTest
    def testcase_delete_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "删除失败，删除运行中的任务"
        # 前提：创建一个处于运行中的固件任务
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().Get_initial_strategy()
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.all_have_link_path)  # 先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        ApiDefine().Start_task(self.session,h,task_id)
        task_id_running = OperationpostgresBase().Sql_connect(2)
        res = ApiDefine().Delete_task(self.session, h, [task_id_running], False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["fail"][0]
        self.assertIn("OK", a)
        self.assertEqual(200, b)
        self.assertIn('处于运行中,不可删除',c)


    @unittest.SkipTest
    def testcase_delete_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "成功删除暂停中的任务"
        # 前提：创建一个处于暂停中的固件任务
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().Get_initial_strategy()
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.all_have_link_path)  # 先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        ApiDefine().Start_task(self.session,h,task_id)   #开始该任务
        ApiDefine().Stop_task(self.session,h,task_id)    #暂停该任务
        res = ApiDefine().Delete_task(self.session, h, [task_id],False)    #删除该任务
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["success"][0]
        self.assertIn("OK", a)
        self.assertEqual(200, b)
        self.assertIn('删除固件扫描任务',c)

    @unittest.SkipTest
    def testcase_delete_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "成功删除不可用的任务"
        # 前提：创建一个不可用的固件任务
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().Get_initial_strategy()
        file_md5 = Get_file_md5(os.path.join(local_config.unavailable_task_path))
        res_ini = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5, local_config.unavailable_task_path)  # 先创建一个任务，获取任务task_id
        task_id = json.loads(res_ini)["data"]["id"]
        ApiDefine().Start_task(self.session,h,task_id)   #开始该任务
        task_id_unavailable = OperationpostgresBase().Sql_connect(4)
        res = ApiDefine().Delete_task(self.session, h, [task_id_unavailable], False)    #删除该任务
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["success"][0]
        self.assertIn("OK", a)
        self.assertEqual(200, b)
        self.assertIn('删除固件扫描任务',c)


    @unittest.SkipTest
    def testcase_delete_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = "删除失败，任务id格式错误"
        h = {"Authorization": Token()}
        res = ApiDefine().Delete_task(self.session, h, [0000000], False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("task_id_list中id参数格式错误", a)
        self.assertEqual(2002, b)


