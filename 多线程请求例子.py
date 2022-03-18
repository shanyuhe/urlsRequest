# 环境python3
import time

import requests
import threading
i = -1
urls_txt = []
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

def logo():
    print("\033[91m[+] Author\033[0m    : 一秋小叶")
    print("\033[91m[+] Email\033[0m     : 2900180755@qq.com")
    print("\033[91m[+] Github\033[0m    : https://github.com/shanyuhe")
    time.sleep(3)

def url_list(txt):
    global urls_txt
    with open(txt, mode='r',encoding='utf-8') as fp:
        urls_txt = fp.readlines()

def return_url():
    global i
    i += 1
    url = urls_txt[i].replace('\n', '').replace('\r', '')
    return url

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            try:
                crawler(return_url(),self.name)
            except:
                break
        print("Thread exit: " + self.name)


# 定义功能函数，访问固定url地址
def crawler(url,ts):
    try:
        r = requests.get(url,headers=header,timeout=20)
        # 打印线程名和响应码
        print(f'{ts} ==> {url} ==> {r.status_code}')
    except Exception as e:
        print(f'{ts} ==> {url} ==> Error')


# 创建线程列表
def goRun(txt,T):
    threads = []
    url_list(txt)
    # 开启线程数量
    print(f'Starting Thread  + {str(T)}')
    for i in range(T):
        # 给每个线程命名
        ts ="Thread-"+str(i)
        thread = myThread(ts)
        thread.start()
        # 将线程添加到线程列表
        threads.append(thread)

    # 等待所有线程完成
    for t in threads:
        t.join()
if __name__ == '__main__':
    logo()
    goRun('./urls.txt',200)



