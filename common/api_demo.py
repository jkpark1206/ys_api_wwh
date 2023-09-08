import requests
from config.config import local_config
from jsonpath import jsonpath

class ApiDefine:

    #登录
    def Login(self,session,data):
        headers = {"Content-Type": "application/json"}
        res = session.post('{}api/user/login'.format(local_config.URL),json=data,headers=headers)
        return res.text


    #修改密码
    def Change_Passwd(self,session,data):
        headers = {"Content-Type": "application/json"}
        res = session.put('{}api/user/login'.format(local_config.URL), json=data, headers=headers)
        return res.text


    #获取token
    def Get_token(self,session):
        data = {"username": local_config.Username,
                "password": local_config.Passwd,
                "anban_password": local_config.Anban_Passwd}
        headers = {"Content-Type":"application/json"}
        res = session.post('{}api/user/login'.format(local_config.URL),json=data,headers=headers)
        token = 'Token '+ jsonpath(res.json(),'$.data.AuthToken')[0]
        return token

    #获取固件分析任务列表
    def Task_list(self,session,data,headers):
        res = session.get('{}api/task/list'.format(local_config.URL),data=data,headers=headers)
        return res.text

    #创建固件扫描分析任务
    def Create_task(self,session,data,headers,file):
        res = session.post('{}api/task/create'.format(local_config.URL),data=data,headers=headers,files=file)
        return res.text

    #创建任务2
    def Create_task_2(self,session,device_name,task_name,vendor,version,plugin,file_md5,task_lib_tag,headers,filepath):
        d = {
            "device_name": device_name,
            "task_name": task_name,
            "vendor": vendor,
            "version": version,
            "plugin": plugin,
            "file_md5": file_md5,
            "task_lib_tag": task_lib_tag
        }
        with open(filepath, 'rb') as firm:
            f = {'firmware': firm}
            res = session.post('{}api/task/create'.format(local_config.URL),data=d,headers=headers,files=f)
        return res.text

    #编辑固件分析任务
    def Fix_task(self,session,task_id,device_name,task_name,vendor,version,plugin,task_lib_tag,headers):
        d = {
            "task_id": task_id,
            "device_name": device_name,
            "task_name": task_name,
            "vendor": vendor,
            "version": version,
            "plugin": plugin,
            "task_lib_tag": task_lib_tag
        }
        res = session.put('{}api/task/create'.format(local_config.URL),data=d,headers=headers)
        return res.text

    #开始固件任务
    def Start_task(self,session,data,headers):
        res = session.put('{}api/task/start'.format(local_config.URL), json=data, headers=headers)
        return res.text

    #暂停固件任务
    def Stop_task(self,session,data,headers):
        res = session.put('{}api/task/stop'.format(local_config.URL) ,json=data , headers=headers)
        return res.text


    #恢复暂停中的固件任务
    def Recover_task(self,session,data,headers):
        res = session.put('{}api/task/recover'.format(local_config.URL),json=data,headers=headers)
        return res.text

    #删除固件任务
    def Delete_task(self,session,data,headers):
        res = session.delete('{}api/task/delete'.format(local_config.URL),json=data,headers=headers)
        return res.text


    #创建对比报告
    def Compare_task(self,session,f_id,s_id,headers):
        data = {
            "first_id": f_id,
            "second_id": s_id
        }
        res = session.post('{}api/compareTask/create'.format(local_config.URL),json=data,headers=headers)
        return res.text


    #删除对比分析报告
    def Del_compare_task(self,session,data,headers):
        res = session.delete('{}api/compareTask/delete'.format(local_config.URL), json=data, headers=headers)
        return res.text

    #创建固件库任务
    def Create_task_lib(self,session,data,headers,file):
        res = session.post('{}api/task_lib/create'.format(local_config.URL), data=data, headers=headers,files=file)
        return res.text


    #下载html固件分析报告（zip文件）
    def Task_report(self,session,data,headers):
        res = session.post('{}api/report_zip'.format(local_config.URL),json=data,headers=headers)
        return res


    #生成pdf报告
    def Start_pdf_report(self,session,data,headers):
        res = session.post('{}api/task/pdf/start'.format(local_config.URL),json=data,headers=headers)
        return res

    #下载pdf报告
    def Download_pdf_report(self,session,data,headers):
        res = session.post('{}api/task/pdf/download'.format(local_config.URL), json=data, headers=headers)
        return res


    #下载系统日志
    def System_log(self,session,data,headers):
        res = session.post('{}api/log/exportfile'.format(local_config.URL),json=data,headers=headers)
        return res   #返回接口的二进制流，数据在二进制流内


    #获取系统日志
    def Get_sys_log(self,session,data,headers):
        res = session.post('{}api/log/systemlist'.format(local_config.URL), json=data, headers=headers)
        return res.text


    #下载用户日志
    def User_log(self,session,data,headers):
        res = session.post('{}api/log/exportfile'.format(local_config.URL),json=data,headers=headers)
        return res   #返回接口的二进制流，数据在二进制流内

    #获取用户日志
    def Get_user_log(self,session,data,headers):
        res = session.post('{}api/log/userlist'.format(local_config.URL), json=data, headers=headers)
        return res.text

    #获取config用户的登录token
    def Get_config_token(self,session):
        data = {"username": "config",
                "password": local_config.Passwd,
                "anban_password": local_config.Anban_Passwd}
        headers = {"Content-Type":"application/json"}
        res = session.post('{}api/user/login'.format(local_config.URL),json=data, headers= headers)
        token = 'Token '+ jsonpath(res.json(),'$.data.AuthToken')[0]
        return token


    #配置产品信息
    def System_config(self,session,headers,data,files):
        res = session.post('{}api/system/config'.format(local_config.URL), headers=headers, data=data,files=files)
        return res.text




# if __name__ =='__main__':
#     session = requests.Session()
    # data = {"username":"wwh",
    #         "password":"fcea920f7412b5da7be0cf42b8c93759",
    #         "anban_password":"f169d2236b9ba09a2ceb8a5c03581d41"}
    # print(type(data))
#
    # print(ApiDefine().Get_config_token(session))

