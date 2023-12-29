import json
from common.session_init import Session_init
from common.api_demo import ApiDefine
import unittest
from common.Random_str import *
from common.Get_token import Token



class Create_Strategy_Test(Session_init):

    # @unittest.skip
    def test_creat_strategy_01(self):
        self._testMethodName = 'case_01'
        self._testMethodDoc = "全选插件创建分析策略-关联固件库-设置默认-配置cvss信息"
        h = {"Authorization": Token()}
        plugin_list = ["soft","sensitive_msg","security","cve","cwe"]
        cvss = {
			  "cve_cdp_2": "N",
			  "cve_td_2": "N",
			  "cve_cr_2": "L",
			  "cve_ir_2": "L",
			  "cve_ar_2": "L",
			  "cve_e_2": "H",
			  "cve_rl_2": "U",
			  "cve_rc_2": "C",
			  "cve_cr_3": "H",
			  "cve_ir_3": "H",
			  "cve_ar_3": "H",
			  "cve_mav_3": "N",
			  "cve_mac_3": "L",
			  "cve_mpr_3": "N",
			  "cve_mui_3": "N",
			  "cve_ms_3": "C",
			  "cve_mc_3": "H",
			  "cve_mi_3": "H",
			  "cve_ma_3": "H",
			  "cve_e_3": "U",
			  "cve_rl_3": "O",
			  "cve_rc_3": "U"
			}
        res = ApiDefine().Analysis_strategy(self.session,h ,Ran_str(1), True, plugin_list, cvss, True)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_strategy_02(self):
        self._testMethodName = 'case_02'
        self._testMethodDoc = "创建成功-只勾选soft插件创建分析策略-名称为单个数字"
        h = {"Authorization": Token()}
        plugin_list = ["soft"]
        res = ApiDefine().Analysis_strategy(self.session,h ,Random_num(),False,plugin_list,None,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_strategy_03(self):
        self._testMethodName = 'case_03'
        self._testMethodDoc = "创建成功-只勾选sensitive_msg插件创建分析策略-名称为64个字符"
        h = {"Authorization": Token()}
        plugin_list = ["sensitive_msg"]
        res = ApiDefine().Analysis_strategy(self.session,h ,Ran_str(64),False,plugin_list,None,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_strategy_04(self):
        self._testMethodName = 'case_04'
        self._testMethodDoc = "创建成功-只勾选security插件创建分析策略"
        h = {"Authorization": Token()}
        plugin_list = ["security"]
        res = ApiDefine().Analysis_strategy(self.session,h ,Ran_str(2),False,plugin_list,None,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


#     # @unittest.skip
    def test_creat_strategy_05(self):
        self._testMethodName = 'case_05'
        self._testMethodDoc = "创建成功-只勾选cve\soft插件创建分析策略"
        h = {"Authorization": Token()}
        plugin_list = ["soft","cve"]
        res = ApiDefine().Analysis_strategy(self.session,h ,Ran_str(2),False,plugin_list,None,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_strategy_06(self):
        self._testMethodName = 'case_06'
        self._testMethodDoc = "创建成功-只勾选cwe插件创建分析策略"
        h = {"Authorization": Token()}
        plugin_list = ["cwe"]
        res = ApiDefine().Analysis_strategy(self.session,h ,Ran_str(2),False,plugin_list,None,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)



    # @unittest.skip
    def test_creat_strategy_07(self):
        self._testMethodName = 'case_07'
        self._testMethodDoc = "创建成功-全选插件不勾选固件库"
        h = {"Authorization": Token()}
        plugin_list = ["soft","sensitive_msg","security","cve","cwe"]
        res = ApiDefine().Analysis_strategy(self.session,h ,Ran_str(2),False,plugin_list,None,False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)



    # @unittest.skip
    def test_creat_strategy_08(self):
        self._testMethodName = 'case_08'
        self._testMethodDoc = "创建失败-策略名称为65个字符"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(65), False, plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_strategy_09(self):
        self._testMethodName = 'case_09'
        self._testMethodDoc = "创建失败-策略名称为空"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, '', False, plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("策略名称参数是必需参数", a)
        self.assertEqual(2000, b)


    # @unittest.skip
    def test_creat_strategy_10(self):
        self._testMethodName = 'case_10'
        self._testMethodDoc = "创建失败-策略名称与已有策略名重复"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, '重复策略', False, plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("策略名称已存在", a)
        self.assertEqual(2002, b)


    # @unittest.skip
    def test_creat_strategy_11(self):
        self._testMethodName = 'case_11'
        self._testMethodDoc = "创建失败-不勾选插件"
        h = {"Authorization": Token()}
        plugin_list = []
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), False, plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("请选择至少一项插件配置", a)
        self.assertEqual(6003, b)


    # @unittest.skip
    def test_creat_strategy_12(self):
        self._testMethodName = 'case_12'
        self._testMethodDoc = "创建失败-lib_tag参数为空"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), '', plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertIs(200, b)


    # @unittest.skip
    def test_creat_strategy_13(self):
        self._testMethodName = 'case_13'
        self._testMethodDoc = "创建失败-cvss_info参数为空"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), False, plugin_list,'', False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)


    # @unittest.skip
    def test_creat_strategy_14(self):
        self._testMethodName = 'case_14'
        self._testMethodDoc = "创建失败-lib_tag为true但插件勾选不完全"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve"]
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), True, plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("插件参数不正确", a)
        self.assertEqual(2002, b)


    # @unittest.skip
    def test_creat_strategy_15(self):
        self._testMethodName = 'case_15'
        self._testMethodDoc = "创建成功-default_tag参数为空"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), False, plugin_list, None,'')
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("OK", a)
        self.assertEqual(200, b)



    # @unittest.skip
    def test_creat_strategy_16(self):
        self._testMethodName = 'case_16'
        self._testMethodDoc = "创建失败-只勾选cve，不勾选soft插件"
        h = {"Authorization": Token()}
        plugin_list = ["sensitive_msg", "security", "cve", "cwe"]
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), False, plugin_list, None, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("插件CVE漏洞查找缺少依赖", a)
        self.assertEqual(2002, b)


    # @unittest.skip
    def test_creat_strategy_17(self):
        self._testMethodName = 'case_17'
        self._testMethodDoc = "创建失败-配置cvss2参数不正确"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        cvss_2 =  {
			  "cve_cdp_2": "T",
			  "cve_td_2": "N",
			  "cve_cr_2": "L",
			  "cve_ir_2": "L",
			  "cve_ar_2": "L",
			  "cve_e_2": "H",
			  "cve_rl_2": "U",
			  "cve_rc_2": "C"
			}
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), False, plugin_list, cvss_2, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("CVSS参数格式错误", a)
        self.assertEqual(2002, b)


    # @unittest.skip
    def test_creat_strategy_18(self):
        self._testMethodName = 'case_18'
        self._testMethodDoc = "创建失败-配置cvss3参数不正确"
        h = {"Authorization": Token()}
        plugin_list = ["soft", "sensitive_msg", "security", "cve", "cwe"]
        cvss_3 = {
              "cve_cr_3": "T",
              "cve_ir_3": "H",
              "cve_ar_3": "H",
              "cve_mav_3": "N",
              "cve_mac_3": "L",
              "cve_mpr_3": "N",
              "cve_mui_3": "N",
              "cve_ms_3": "C",
              "cve_mc_3": "H",
              "cve_mi_3": "H",
              "cve_ma_3": "H",
              "cve_e_3": "H",
              "cve_rl_3": "U",
              "cve_rc_3": "C"
			}
        res = ApiDefine().Analysis_strategy(self.session, h, Ran_str(2), False, plugin_list, cvss_3, False)
        a = json.loads(res)["message"]
        b = json.loads(res)["code"]
        self.assertIn("CVSS参数格式错误", a)
        self.assertEqual(2002, b)
