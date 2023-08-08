import psycopg2
from config.config import local_config
import os
import loguru
import time


class OperationpostgresBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
            host = local_config.host,
            port = local_config.port,
            user = local_config.user,
            password = local_config.password,
            database = local_config.databases
            )
        except Exception as e:
            loguru.logger.info(e)
        self.cur = self.conn.cursor()

    def Sql_connect(self,s):
        try:
            self.cur.execute("select id,task_name from ys_firmware_scan_task where task_status = {} and is_delete='f' order by id desc limit 1".format(s))
            task_list = self.cur.fetchall()
            if len(task_list)==0:  #未查找到相应状态的任务，则执行以下相应操作
                # if s == 1:  #查找队列中的任务
                #     self.cur.execute("select * from ys_firmware_scan_task where task_status = {} and is_delete='f'  limit 1".format(s))
                #     task_list = self.cur.fetchall()
                #     task_id = task_list[0][0]
                #     return task_id
                if s == 2:  #查找运行中的任务
                    while True:
                        self.cur.execute("select id,task_name from ys_firmware_scan_task where task_status = {} and is_delete='f' order by id desc limit 1".format(s))
                        task_list = self.cur.fetchall()
                        if len(task_list) != 0:
                            task_id = task_list[0][0]
                            return task_id
                        else:
                            #"强制等待1分钟,等待任务状态变为运行中!"
                            loguru.logger.info("强制等待5s,等待任务状态变为运行中!")
                            time.sleep(5)

                if s == 3:  #查找已结束的任务
                    while True:
                        self.cur.execute("select * from ys_firmware_scan_task where task_status = {} and is_delete='f' order by id desc limit 1".format(s))
                        task_list = self.cur.fetchall()
                        if len(task_list)!=0:
                            task_id = task_list[0][0]
                            return task_id
                        else:
                            # 强制等待1分钟，直到任务结束
                            loguru.logger.info("强制等待1分钟,等待任务结束!")
                            time.sleep(60)

                if s == 4: #查找不可用的任务
                    while True:
                        self.cur.execute(
                            "select * from ys_firmware_scan_task where task_status = {} and is_delete='f' order by id desc limit 1".format(s))
                        task_list = self.cur.fetchall()
                        if len(task_list) != 0:
                            task_id = task_list[0][0]
                            return task_id
                        else:
                            # 强制等待2分钟，直到任务结束
                            loguru.logger.info("强制等待1分钟,等待任务结束!")
                            time.sleep(60)
            else:  #若存在相应状态的任务，则直接返回任务id
                task_id = task_list[0][0]
                return task_id
            self.cur.close()

        except Exception as e:
            loguru.logger.info(e)
            self.cur.close()
    def Finished_task(self):
        self.cur.execute(
            "select id,task_name from ys_firmware_scan_task where task_status = 3 and is_delete='f' order by id desc Limit 2")
        task_id = self.cur.fetchall()
        return task_id

    def Get_Compare_Task(self):
        self.cur.execute(
            "select id from ys_report_compare where task_status = 3 and is_delete='f' order by id desc Limit 6")
        task_id = self.cur.fetchall()
        return task_id

if __name__=='__main__':
    print(OperationpostgresBase().Sql_connect(2))




