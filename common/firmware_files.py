from config.config import local_config
class Upload_files:
    def Upload_Firmware(self,file_path):
        firmware_files =open(file_path,'rb')
        print(firmware_files)

    def Upload_Cve_file(self,cve_path):
        cve_file = [('cve',('上传cve', open(cve_path,'rb'),'application/octet-stream'))]
        return cve_file

if __name__ == '__main__':
    Upload_files().Upload_Cve_file(local_config.all_have_path)


