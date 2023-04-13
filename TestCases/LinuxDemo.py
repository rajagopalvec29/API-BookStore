import paramiko as paramiko
from Utilities.Configuration import *


host = getConfig()['SSH']['host']
port = getConfig()['SSH']['port']
username = getConfig()['SSH']['username']
password = getConfig()['SSH']['password']

#SSH Connect
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

#Execute Commands
stdio,stdout,stderr = ssh.exec_command("cat Demofile")
rows = stdout.readlines()
for i in rows:
    print(i)

#File Transfer
sftp = ssh.open_sftp()
destinationPath = "script.py"
LocalPath = "C:\\Users\\Admin\\PycharmProjects\\API_BookStore\\Batchfiles\\script.py"
# sftp.put(LocalPath,destinationPath)

sftp.get('loanasa.csv','C:\\Users\\Admin\\PycharmProjects\\API_BookStore\\Outputfiles\\loanupdated.csv')

#Run Batch Files
# stdio,stdout,stderr = ssh.exec_command("python script.py")
