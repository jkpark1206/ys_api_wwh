from jsonpath import jsonpath
import requests
from loguru import logger
from config.config import local_config

class APIDefine:
    AuthToken = ''
    def __init__(self):
        #实例化一个session类
        self.session = requests.session()
        # 实例化一个请求头
        self.session.headers = {"Content-Type":"application/json"}
        # 设置全局通用的请求url
        self.base_url = local_config.URL


    def get_authToken(self):
        #获取token值APIDefine.AuthToken
        method = "post"
        url = local_config.URL+'/api/user/login'
        data = {"username":local_config.Username,"password":local_config.Passwd,"anban_password":local_config.Anban_Passwd}
        res = self.session.request(method,url, json = data,headers=self.session.headers)

        #赋予类变量APIDefine.AuthToken的值为提取的token值
        APIDefine.AuthToken = 'Token ' + jsonpath(res.json(), '$.data.AuthToken')[0]
        return APIDefine.AuthToken


    def send_req(self,method,url,data,**kwargs):
        self.__header(APIDefine.AuthToken)
        if method.upper() == "GET":
            res = self.session.get(self.base_url+url, json=data, **kwargs)
            logger.info(f"请求url为：{self.base_url+url}")
            logger.info(f"请求method为：{method}")
            logger.info(f"请求datas为：{data}")
            logger.info(f"请求headers为：{self.session.headers}")
            return res

        else:
            res = self.session.request(method,self.base_url+url,json=data,headers=self.session.headers)
            logger.info(f"请求url为：{self.base_url+url}")
            logger.info(f"请求method为：{method}")
            logger.info(f"请求datas为：{data}")
            logger.info(f"请求headers为：{self.session.headers}")
            return res

    def __header(self,token):
        if token:
            self.session.headers["Authorization"] = token

# if __name__ == '__main__':
#     APIDefine().get_authToken()  #移到了handle_yaml,将token写入了yaml文件中，并进行了读取
#     method='post'
#     url = 'http://192.168.5.253:8011/api/task/list'
#     param = {"page": "1",
#             "limit":100,
#             "keywords":"",
#             "sort_by":0,
#             "task_status_list":[0,1,2,3,4,5],
#             "vendor_keywords":"",
#             "start_time":"2022-06-27 17:39:20",
#             "end_time":"2023-10-30 17:39:19"}
#     APIDefine().send_req(method,url,param)









