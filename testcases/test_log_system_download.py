import unittest
from config.config import local_config
from common.session_init import Session_init
from common.api_demo import ApiDefine
from zipfile import ZipFile
from io import BytesIO
import json

class Log_system_test(Session_init):

    # @unittest.skip
    def test_log_sys_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = '成功下载系统日志'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        d = {"log_tag":1,     #此字段是系统日志
            "start_time":"2023-07-01 14:46:20",
            "end_time":"2024-08-28 14:46:31"
	        }
        res = ApiDefine().System_log(self.session,d,h)  #接口返回的内容为二进制流
        file = res.content    #二进制流内的数据
        zipped_data = ZipFile(BytesIO(file))     #使用ZipFile将二进制流写入zipped_data中
        zipped_data.extractall(local_config.Log_system_file)    #使用extractall将zipped_data文件解压，
                                                                # 存在local_config.Log_system_file该文件夹中，可去文件夹内查看日志内容




    # @unittest.skip
    def test_log_sys_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = '下载系统日志失败-选择不存在日志记录的时间'
        token = ApiDefine().Get_token(self.session)
        h = {'Authorization': token}
        d = {"log_tag": 1,
            "start_time": "2022-10-07 14:46:20",
            "end_time": "2022-10-07 14:46:20"
                     }
        res = ApiDefine().System_log(self.session, d, h).text  # 接口返回的内容为二进制流
        a = json.loads(res)["code"]
        b = json.loads(res)["message"]
        self.assertEqual(7009, a)
        self.assertEqual("没有符合条件的日志文件", b)


