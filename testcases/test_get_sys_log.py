import json
import unittest

from common.session_init import Session_init
from common.api_demo import ApiDefine


class Get_sys_log(Session_init):

    # @unittest.skip
    def test_get_syslog_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功获取系统日志'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        d = {
            "page": 1,
            "limit": 100,
            "keywords": "",
            "sort_by": 0,
            "start_time": "2023-12-01 00:00:00",
            "end_time": "2024-01-06 23:59:59"
        }
        res = ApiDefine().Get_sys_log(self.session,d,h)
        a = json.loads(res)["code"]
        b = json.loads(res)["message"]
        self.assertEqual(200,a)
        self.assertIn("OK",b)






