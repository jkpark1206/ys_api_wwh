import json
from common.session_init import Session_init
from common.api_demo import ApiDefine
from config.config import local_config
from common.Md5_data import Get_file_md5
import os
from common.Get_token import Token
from common.database_datas import OperationpostgresBase

class Create_Firmware_Task_Test(Session_init):

    # @unittest.skip
    def test_creat_task_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "全选插件上传固件任务"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.maxstr_task_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_all)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.maxstr_task_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)



    # @unittest.skip
    def test_creat_task_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "创建关联固件库任务"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        s_id = OperationpostgresBase().lib_strategy_id()
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)


    # @unittest.skip
    def test_creat_task_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "创建成功-只勾选cwe"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_cwe)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)


    # @unittest.skip
    def test_creat_task_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "创建成功-只勾选cve\soft"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_cve_soft)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)



    # @unittest.skip
    def test_creat_task_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "创建成功-只勾选soft"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_soft)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)



    # @unittest.skip
    def test_creat_task_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "创建成功-只勾选security"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_security)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)


    # @unittest.skip
    def test_creat_task_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "创建成功-只勾选sensitive_msg"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.initial_task_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_sensitive_msg)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.initial_task_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(200, a)
        self.assertIn("OK", b)


    # @unittest.skip
    def test_creat_task_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "创建失败-分析策略为空"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        res = ApiDefine().Create_Firmware_Task(self.session, h, '', file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2002, a)
        self.assertIn("参数类型错误！", b)


    # @unittest.skip
    def test_creat_task_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = "创建失败-任务名为100个字符"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.overstr_task_path))
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_all)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.overstr_task_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2005, a)
        self.assertIn("任务文件名超出最大长度", b)


    # @unittest.skip
    def test_creat_task_11(self):
        self._testMethodName = 'case_11'
        self._testMethodDoc = "创建失败-MD5与文件不符"
        h = {"Authorization": Token()}
        file_md5 = 'e8422a56f8eadb1cfac4bd68581dec78'
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_all)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(5004, a)
        self.assertIn("上传的固件libcurl_7.17.1-1_arm.ipk不完整", b)


    # @unittest.skip
    def test_creat_task_12(self):
        self._testMethodName = 'case_12'
        self._testMethodDoc = "创建失败-MD5为空"
        h = {"Authorization": Token()}
        s_id = OperationpostgresBase().all_strategy_id(local_config.plugin_all)
        res = ApiDefine().Create_Firmware_Task(self.session, h, s_id,'',local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(2002, a)
        self.assertIn("文件MD5值不合法", b)


    # @unittest.skip
    def test_creat_task_13(self):
        self._testMethodName = 'case_13'
        self._testMethodDoc = "创建失败-strategy_id为不存在的id"
        h = {"Authorization": Token()}
        file_md5 = Get_file_md5(os.path.join(local_config.all_have_link_path))
        res = ApiDefine().Create_Firmware_Task(self.session, h, 0, file_md5,local_config.all_have_link_path)
        a = json.loads(res)['code']
        b = json.loads(res)['message']
        self.assertEqual(3001, a)
        self.assertIn("策略不存在", b)

