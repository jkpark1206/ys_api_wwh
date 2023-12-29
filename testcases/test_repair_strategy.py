import unittest
from common.Md5_data import Get_file_md5
import json
from config.config import local_config
from common.api_demo import ApiDefine
from common.session_init import Session_init
from common.database_datas import OperationpostgresBase
import os
from common.Random_str import *
from common.Get_token import Token


class Repair_Strategy_Test(Session_init):

	# @unittest.skip
	def test_repair_strategy_01(self):
		self._testMethodName = 'case_01'
		self._testMethodDoc = '成功修改分析策略-策略名为单个字母'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		cvss_info = {"cve_cdp_2": "N",
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
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(1),True,cvss_info,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)


	# @unittest.skip
	def test_repair_strategy_02(self):
		self._testMethodName = 'case_02'
		self._testMethodDoc = '成功修改分析策略-策略名为单个数字-只勾选soft插件'
		h = {"Authorization": Token()}
		plugin_list = ["soft"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Random_num(),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)


	# @unittest.skip
	def test_repair_strategy_03(self):
		self._testMethodName = 'case_03'
		self._testMethodDoc = '成功修改分析策略-只勾选cve\soft插件'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)


	# @unittest.skip
	def test_repair_strategy_04(self):
		self._testMethodName = 'case_04'
		self._testMethodDoc = '成功修改分析策略-只勾选cwe插件'
		h = {"Authorization": Token()}
		plugin_list = ["cwe"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)


	# @unittest.skip
	def test_repair_strategy_05(self):
		self._testMethodName = 'case_05'
		self._testMethodDoc = '成功修改分析策略-只勾选security插件'
		h = {"Authorization": Token()}
		plugin_list = ["security"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)



	# @unittest.skip
	def test_repair_strategy_06(self):
		self._testMethodName = 'case_06'
		self._testMethodDoc = '成功修改分析策略-只勾选sensitive_msg插件'
		h = {"Authorization": Token()}
		plugin_list = ["sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)


	# @unittest.skip
	def test_repair_strategy_07(self):
		self._testMethodName = 'case_07'
		self._testMethodDoc = '修改失败-勾选cve插件但未勾选soft插件'
		h = {"Authorization": Token()}
		plugin_list = ["cve"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("插件CVE漏洞查找缺少依赖", b)


	# @unittest.skip
	def test_repair_strategy_08(self):
		self._testMethodName = 'case_08'
		self._testMethodDoc = '修改失败-lib_tag为true,但插件勾选不完全'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),True,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("插件参数不正确", b)


	# @unittest.skip
	def test_repair_strategy_09(self):
		self._testMethodName = 'case_09'
		self._testMethodDoc = '修改失败-plugin_list为空'
		h = {"Authorization": Token()}
		plugin_list = []
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),False,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(6003,a)
		self.assertIn("请选择至少一项插件配置", b)



	# @unittest.skip
	def test_repair_strategy_10(self):
		self._testMethodName = 'case_10'
		self._testMethodDoc = '修改失败-策略id不存在'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),True,None,True,plugin_list,100000)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(3001,a)
		self.assertIn("策略不存在", b)


	# @unittest.skip
	def test_repair_strategy_11(self):
		self._testMethodName = 'case_11'
		self._testMethodDoc = '修改失败-策略id为空'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),True,None,True,plugin_list,'')
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("参数类型错误！", b)


	# @unittest.skip
	def test_repair_strategy_12(self):
		self._testMethodName = 'case_12'
		self._testMethodDoc = '修改失败-cvss2参数值错误'
		h = {"Authorization": Token()}
		cvss2 =  {
			  "cve_cdp_2": "T",
			  "cve_td_2": "N",
			  "cve_cr_2": "L",
			  "cve_ir_2": "L",
			  "cve_ar_2": "L",
			  "cve_e_2": "H",
			  "cve_rl_2": "U",
			  "cve_rc_2": "C"
			}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),True,cvss2,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("CVSS参数格式错误", b)



	# @unittest.skip
	def test_repair_strategy_13(self):
		self._testMethodName = 'case_13'
		self._testMethodDoc = '修改失败-cvss3参数值错误'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		cvss3 = {"cve_cr_3": "TT",
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
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),True,cvss3,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("CVSS参数格式错误", b)



	# @unittest.skip
	def test_repair_strategy_14(self):
		self._testMethodName = 'case_14'
		self._testMethodDoc = '修改失败-策略名称为101个字符'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(101),True,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2000,a)
		self.assertIn("策略名称参数长度错误,最大长度为100", b)


	# @unittest.skip
	def test_repair_strategy_15(self):
		self._testMethodName = 'case_15'
		self._testMethodDoc = '修改失败-策略名称为空'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,'',True,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2000,a)
		self.assertIn("策略名称参数是必需参数", b)


	# @unittest.skip
	def test_repair_strategy_16(self):
		self._testMethodName = 'case_16'
		self._testMethodDoc = '修改成功-策略名称为100个字符'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(100),True,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(200,a)
		self.assertIn("OK", b)


	# @unittest.skip
	def test_repair_strategy_17(self):
		self._testMethodName = 'case_17'
		self._testMethodDoc = '修改失败-策略名称与已有策略名称重复'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_strategy_id()
		res = ApiDefine().Fix_strategy(self.session,h,'重复策略',True,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("策略名称已存在", b)


	# @unittest.skip
	def test_repair_strategy_18(self):
		self._testMethodName = 'case_18'
		self._testMethodDoc = '修改失败-内置策略不可修改'
		h = {"Authorization": Token()}
		plugin_list = ["soft","cve","cwe","security","sensitive_msg"]
		s_id = OperationpostgresBase().Get_initial_strategy()
		res = ApiDefine().Fix_strategy(self.session,h,Ran_str(2),True,None,True,plugin_list,s_id)
		a = json.loads(res)['code']
		b = json.loads(res)['message']
		self.assertEqual(2002,a)
		self.assertIn("默认策略无法修改", b)

