import os
import time


class config:
    def __init__(self):#获取当前文件的父目录路径(C:\yishi_2\自动化测试\ys_api_wwh\config)config包的路径
        self.parent_path = os.path.dirname(os.path.realpath(__file__))

# 配置URL地址
    @property
    def URL(self):
        return 'http://192.168.1.208:8011/'

# 配置用户登录名、密码
    @property
    def Username(self):
        return 'wwh'

    @property
    def Passwd(self):
        return 'fcea920f7412b5da7be0cf42b8c93759'

    @property
    def Anban_Passwd(self):
        return 'f169d2236b9ba09a2ceb8a5c03581d41'

#配置连接数据库相关信息
    @property
    def host(self):
        return '192.168.1.208'

    @property
    def port(self):
        return 25432

    @property
    def user(self):
        return 'postgres'

    @property
    def password(self):
        return 123456

    @property
    def databases(self):
        return 'ys_yishi'

#测试用例放置文件夹路径
    @property
    def dir_testcase(self):
        return os.path.dirname(self.parent_path)+'\\testcases'

#生成报告放置的目录
    @property
    def Report_Dir(self):
        return os.path.dirname(self.parent_path)+'\\reports\\'

# 生成报告放置的目录
    @property
    def Test_Log_dir(self):
        return os.path.dirname(self.parent_path) + '\\Test_log\\'

# 生成固件列表CSV文件的地址
    @property
    def Firmware_csv_path(self):
        return self.parent_path+'\\firmware_list.csv'

#测试固件放置目录
    @property
    def Firmware_path(self):
        return os.path.dirname(self.parent_path)+'\\firmware\\测试固件'

#全选插件固件
    @property
    def all_have_path(self):
        return os.path.dirname(self.parent_path)+'\\firmware\\测试固件\\libcrypto.so.0.9.8'

#关联固件库插件
    @property
    def all_have_link_path(self):
        return os.path.dirname(self.parent_path)+'\\firmware\\测试固件\\libcurl_7.17.1-1_arm.ipk'

#初始状态任务固件
    @property
    def initial_task_path(self):
        return os.path.dirname(self.parent_path)+'\\firmware\\测试固件\\zsy.zip'

#暂停状态的固件
    @property
    def stop_task_path(self):
        return os.path.dirname(self.parent_path)+'\\firmware\\测试固件\\libcrypto.so.0.9.8'

#不可用固件
    @property
    def unavailable_task_path(self):
        return os.path.dirname(self.parent_path) + '\\firmware\\测试固件\\dsp.ko'

# 65个字符固件
    @property
    def overstr_task_path(self):
        return os.path.dirname(self.parent_path) + '\\firmware\\测试固件\\提升品型的权威机携手飒飒1开展识传播1的1公益!合-展知识播公益展#识传播的公益展知发知识传播的公益展知识传播的公益展知发传播的公益展知发知识传播的公益展知识传播的公益展知发111111111.ipk'

# 64个字符固件
    @property
    def maxstr_task_path(self):
        return os.path.dirname(self.parent_path) + '\\firmware\\测试固件\\提升品型的权威机携手飒飒开展识传播1的1公益!合-展知识播公益展#识传播的公益展知发知识传播的公益展知识传播的公益展知发.ipk'

    #特斯拉大固件
    @property
    def ota_firmware(self):
        return 'E:\\易识\\特斯拉20220315112226_64G.rar'

#勾选不同插件
    @property
    def Plugin_All(self):
        return '''["cwe_checker","software_components","cve_lookup","crypto_hints","sensitive_msg","users_and_passwords","elf_checksec"]'''


    @property
    def Plugin_Cwe0(self):
        return  '''["software_components","cve_lookup","crypto_hints","elf_analysis","sensitive_msg","elf_checksec"]'''


    @property
    def Plugin_Cve0(self):
        return  '''["cwe_checker","software_components","crypto_hints","elf_analysis","sensitive_msg","elf_checksec"]'''

    @property
    def Plugin0(self):
        return  '''[]'''


    @property
    def Log_system_file(self):
        cur_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        log_file_sys = os.path.dirname(self.parent_path)+'\\Log\\{}syslog'.format(cur_time)
        return log_file_sys

    @property
    def Log_user_file(self):
        cur_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        log_file_user = os.path.dirname(self.parent_path)+'\\Log\\{}userlog'.format(cur_time)
        return log_file_user

    @property
    def Logo_normal_logo_path(self):
        return os.path.dirname(self.parent_path)+'\\Logo_file\\安般易识蓝色logo.svg'

    @property
    def Logo_white_logo_path(self):
        return os.path.dirname(self.parent_path)+'\\Logo_file\\安般易识白色logo.svg'


    @property
    def Logo_web_logo_path(self):
        return os.path.dirname(self.parent_path)+'\\Logo_file\\browser_logo.ico'


    @property
    def Logo_watermark_logo_path(self):
        return os.path.dirname(self.parent_path)+'\\Logo_file\\watermark_logo.png'

    @property
    def Logo_svg_over_path(self):
        return os.path.dirname(self.parent_path)+'\\Logo_file\\超2M的svg图片.svg'

    @property
    def Logo_png_over_path(self):
        return os.path.dirname(self.parent_path)+'\\Logo_file\\超大PNG图片.png'



local_config = config()

# if __name__ == '__main__':
#     print(local_config.Logo_normal_logo_path)

# a = os.path.dirname(os.path.realpath(__file__))
# b = os.path.dirname(a)
# print(a,b)