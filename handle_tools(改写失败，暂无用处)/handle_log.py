import os
import time
from loguru import logger
from config.config import local_config
from faker import Faker

# 获取当前时间# 获取当前时间
cur_time=time.strftime("%Y%m%m-%H%M%S",time.localtime())

# 添加日志输出到文件
logger.add(os.path.join(local_config.Test_Log_dir,"api_log",f"api-{cur_time}.log"), encoding='utf-8', backtrace=True, diagnose=True, retention="30 days", rotation="1 week")
# print(os.path.join(local_config.Test_Log_dir,"api_log",f"api-{cur_time}.log"))




faker = Faker()

name = faker.name()
address = faker.address()
phone = faker.pystr()

print(phone)



