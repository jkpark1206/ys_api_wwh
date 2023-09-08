import json
import unittest
from common.api_demo import ApiDefine
from common.session_init import Session_init
from common.database_datas import OperationpostgresBase
from common.Get_token import Token


class Del_compare_task(Session_init):

    # @unittest.skip
    def test_del_Ctask_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功删除单个对比分析报告'
        h = {"Authorization": Token()}
        task_id = OperationpostgresBase().Get_Compare_Task()[0][0]
        d = {"task_id_list":[task_id]}
        res = ApiDefine().Del_compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["success"][0]
        self.assertIn('OK',a)
        self.assertEqual(200,b)
        self.assertIn('成功', c)


    # @unittest.skip
    def test_del_Ctask_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = '成功删除多个对比分析报告'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        #前提：创建多个对比任务
        f_id = OperationpostgresBase().Finished_task()[0][0]
        s_id = OperationpostgresBase().Finished_task()[1][0]
        ApiDefine().Compare_task(self.session, f_id,s_id, h)
        ApiDefine().Compare_task(self.session, f_id,s_id, h)
        task_id_1 = OperationpostgresBase().Get_Compare_Task()[0][0]
        task_id_2 = OperationpostgresBase().Get_Compare_Task()[1][0]
        d = {"task_id_list":[task_id_1,task_id_2]}
        res = ApiDefine().Del_compare_task(self.session,d,h)
        try:
            a = json.loads(res)["message"]
            b = json.loads(res)["code"]
            c = json.loads(res)["data"]["success"][0]
            self.assertIn('OK',a)
            self.assertEqual(200,b)
            self.assertIn('成功',c)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_del_Ctask_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = '删除对比分析报告失败-任务id不存在'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {"task_id_list":[11111111111]}
        res = ApiDefine().Del_compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        c = json.loads(res)["data"]["fail"]
        self.assertIn('OK',a)
        self.assertEqual(200,b)
        self.assertIn(11111111111, c)


    # @unittest.skip
    def test_del_Ctask_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = '删除对比分析报告失败-任务id为空'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization": token}
        d = {"task_id_list":[]}
        res = ApiDefine().Del_compare_task(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn('缺少task_id_list参数',a)
        self.assertEqual(2001,b)

