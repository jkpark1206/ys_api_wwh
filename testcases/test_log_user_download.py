import unittest

from common.session_init import Session_init
from common.api_demo import ApiDefine
from zipfile import ZipFile
from io import BytesIO
import json
from config.config import local_config


class Log_user_test(Session_init):

    # @unittest.skip
    def test_log_user_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功下载用户日志'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization":token}
        d = {
            "log_tag":2,    #此字段是用户日志
            "start_time":"2023-07-01 14:46:20",
            "end_time":"2024-10-28 14:46:31"
        }
        res = ApiDefine().User_log(self.session,d,h)
        file = res.content
        fileData = ZipFile(BytesIO(file))
        fileData.extractall(local_config.Log_user_file)
        try:
            a = res.status_code
            self.assertEqual(200,a)
        except Exception as e:
            print(e)


    # @unittest.skip
    def test_log_user_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = '下载用户日志失败-该时段无用户日志信息'
        token = ApiDefine().Get_token(self.session)
        h = {"Authorization":token}
        d = {
            "log_tag":2,    #此字段是用户日志
            "start_time":"2022-07-01 14:46:20",
            "end_time":"2022-10-28 14:46:31"
        }
        res = ApiDefine().User_log(self.session,d,h).text
        try:
            a = json.loads(res)["code"]
            b = json.loads(res)["message"]
            self.assertEqual(7009,a)
            self.assertIn("没有符合条件的日志文件",b)
        except Exception as e:
            print(e)










