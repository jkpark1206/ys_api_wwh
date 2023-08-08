# -*- coding:utf-8 -*-
import json
import os, yaml
from common.api_define import APIDefine
from loguru import logger


#将生成的token写入yaml文件中，再读取出来
def get_yaml():
    cur = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
    yaml_path = os.path.join(cur, "../common/token.yaml")  # 获取yaml文件的路径print(yaml_path)
    t0 = APIDefine().get_authToken()
    t = {"token": t0}  # 写入的内容
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(t , stream=f,allow_unicode=True)
        #读取yaml内容
    f = open(yaml_path, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg, Loader=yaml.FullLoader)
    d1 = d["token"]
    return d1


class Handle_yaml:
    def __init__(self,yaml_path):
        # try:
            self.yaml_path = yaml_path
        #     logger.info(f"上传文件路径为:{yaml_path}")
        #
        # except:
        #     logger.exception(f"上传文件失败，请检查路径")

    def read_yaml(self):
        with open(self.yaml_path,encoding="utf-8") as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value

# n=0
# A= [1,2]
# for n in range(0,len(A)):
#     data = A[n]
#     n= n+1



    # def get_datas(self):
    #     cur = os.path.dirname(os.path.realpath(__file__))
    #     sh = (os.path.join(cur, "Atestcases.yaml")



"""
用load转字典
yaml5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，通过默认加载器（FullLoader）禁止执行任意函数
Loader=yaml.FullLoader 加上这行代码，告警就没了"""


if __name__ == '__main__':
    # A = Handle_yaml("C:\\yishi_2\\自动化测试\\ys_api_wwh\\testcases\\Atestcases.yaml").read_yaml()
    # print(A)
    get_yaml()

