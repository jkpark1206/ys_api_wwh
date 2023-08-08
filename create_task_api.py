# -- coding: utf-8 --**

import requests
from jsonpath import jsonpath
from common.Md5_data import Get_file_md5
import os
import hashlib
import json
#v2.10插件
#plugin = '''["software_components","cve_lookup","crypto_hints","elf_analysis","elf_checksec","sensitive_msg"]'''

plugin = '''["cwe_checker","software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]'''
#plugin = '''["software_components"]'''
#艾拉比插件cwe0
#plugin = '''["software_components","cve_lookup","crypto_hints","elf_analysis","ip_and_uri_finder","users_and_passwords","elf_checksec"]'''

URL ='http://192.168.1.208:8011/'

l=[]
#1、修改此处的文件路径,读取该路径下所有固件
for filename in os.listdir(r'C:\\Users\\Administrator\\Desktop\\gujianhuizong\\jizhunceshi'):
    l.append('C:\\Users\\Administrator\\Desktop\\gujianhuizong\\jizhunceshi\\'+filename)


# for filename in os.listdir(r'E:\\易识\\固件适配类型\\QNX'):
#     l.append('E:\\易识\\固件适配类型\\QNX\\'+filename)
    #E:\易识\固件适配类型\QNX

# for filename in os.listdir(r'E:\\易识\\网关、采集器固件（含内蒙古电力项目）\\内蒙古电科项目客户提供\\安全测试用固件汇总'):
#     l.append('E:\\易识\\网关、采集器固件（含内蒙古电力项目）\\内蒙古电科项目客户提供\\安全测试用固件汇总\\'+filename)

#2、查找目录下以特定后缀结尾的文件  修改floder和extension（后缀）即可  n限制取文件的个数（n1=0,n2=51,从第1个开始取到第50个文件）
# floder = "E:\\download\\completed"
# extension = ".hex"
# n1 = 61
# n2 = 81
#
# for root, dirs, files in os.walk(floder):
#     for file in files:
#         if file.endswith(extension):
#            l.append(os.path.join(root, file))
#     l = l[n1:n2]


#3、读取文件夹下所有文件，查到是目录则继续遍历，直到读取完该目录下所有的文件，返回所有文件路径
def traverse_folder(path) :
    for file_name in os.listdir(path):#获取当前目录下所有文件和文件夹的名称
        file_path=os.path.join(path,file_name)#将文件名和路径连接起来
        if os.path.isdir(file_path):#判断该路径是否为文件夹
            # print("文件夹:",file_name)
            traverse_folder(file_path)#如果是文件夹,则递归调用该函数
        else:
            # print(file_path)
            l.append(file_path)
    return l
# traverse_folder('C:\\Users\\Administrator\\Desktop\\gujianhuizong\\jizhunceshi')
# for i in l:
#     a = i.split('\\')[-1]
#     print(a)








def Get_file_md5(file_path):
    try:
        with open(file_path,'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            hash_value = md5obj.hexdigest()
            return hash_value
    except Exception as e:
        print('ERROR', f'获取文件{file_path}md5值出错,原因{e}')


class Upload_firmware:
    def __init__(self):
        self.session = requests.session()
        data = {"username": 'wwh',
                "password": '126cfbcd4d16ae6d25c9bfcae76d8ee4',
                "anban_password": '6b5c557da96612408d2844af0d9f5e5d'}
        headers = {"Content-Type": "application/json"}
        res = self.session.post('{}api/user/login'.format(URL), json=data, headers=headers)
        self.token = 'Token ' + jsonpath(res.json(), '$.data.AuthToken')[0]

    def Create_firmtask(self):
        try:
            for firm_path in l:
                file_md5 = Get_file_md5(os.path.join(firm_path))
                task_name = firm_path.split('\\')[-1]
                h = {"Authorization": self.token}
                d = {"device_name": task_name,
                     "task_name": task_name,
                     "vendor": 'test',
                     "version": 'test',
                     "plugin": plugin,
                     "file_md5": file_md5,
                     "task_lib_tag": "false"
                     }
                with open(firm_path, 'rb') as file:
                    f = {'firmware': file}
                    res2 = self.session.post('{}api/task/create'.format(URL),data= d,headers=h,files=f)
                    task_id = json.loads(res2.text)["data"]["id"]
                    d2 = {"task_id": task_id}
                    res3 = self.session.post('{}api/task/start'.format(URL), json=d2, headers=h)
                    print(res3.text)
        except Exception as e:
                print(e)



if __name__ == '__main__':
    # traverse_folder('C:\\Users\\Administrator\\Desktop\\gujianhuizong\\jizhunceshi')
    Upload_firmware().Create_firmtask()





