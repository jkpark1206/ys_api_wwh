import json
from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
import unittest
from common.Random_str import Ran_str

class Fix_Task_Test(Session_init):
    # @unittest.skip
    def test_Fix_task_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "修改任务只勾选插件"
        token = ApiDefine().Get_token(self.session)
        task_name = '全选插件创建任务'
        h = {"Authorization": token}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_path))
        with open(local_config.all_have_path, 'rb') as firm:
            f = {'firmware': firm}
            res =  ApiDefine().Create_task_2(self.session,task_name,task_name,'all','all',local_config.Plugin_All,file_md5,'false', h, f)
            task_id = int(json.loads(res)["data"]["id"])
            print(task_id)
            res_2 = ApiDefine().Fix_task(self.session,task_id,task_name,task_name,'all','all',local_config.Plugin_All,h)
            try:
                a = json.loads(res_2)["message"]
                b = json.loads(res_2)["code"]
                self.assertIn("OK", a)
                self.assertIs(200, b)
            except Exception as e:
                print(e)
