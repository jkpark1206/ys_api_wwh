import json
import unittest
from common.session_init import Session_init
from common.api_demo import ApiDefine


class Task_List_Test(Session_init):
#用例1：成功获取任务列表
    # @unittest.SkipTest
    def test_get_task_list_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "获取任务列表"
        token = ApiDefine().Get_token(self.session)
        h={"Authorization":token}
        d = {"page": "1",
            "limit":100,
            "keywords":"",
            "sort_by":0,
            "task_status_list":[0,1,2,3,4,5],
            "vendor_keywords":"",
            "start_time":"2022-06-27 17:39:20",
            "end_time":"2024-10-30 17:39:19"}
        res = ApiDefine().Task_list(self.session,d,h)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK",a)
        self.assertIs(200,b)