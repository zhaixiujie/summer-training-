# 导入多线程库
from threading import Thread
import requests
import time
# 存放不同Ip
ip_list=['118.20.1.1','222.222.222.222','111.111.111.111']
# 子进程要执行的代码
def getip(ip):
    r=requests.get(f'http://freeapi.ipip.net/{ip}')
    print(time.ctime(),r.text)

if __name__=='__main__':
    
    #task存放所有的任务
    task=[]
    #循环创建并放入任务池
    for ip in ip_list:
        #创建线程
        t=Thread(target=getip,args=(ip,))
        #放入任务池
        task.append(t)
        t.start()
    # 开始所有任务
    for t in task:
        t.join()
        