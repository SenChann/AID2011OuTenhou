"""
线程创建示例1
"""
import threading
from time import sleep
import os

a = 1


# 线程函数
def music():
    global a
    for i in range(3):
        a = 10000
        sleep(2)
        print(os.getppid(), os.getpid(), "播放：黄河大合唱")


thread = threading.Thread(target=music)
thread.start()

for i in range(4):
    sleep(1)
    print(os.getppid(), os.getpid(), "播放：葫芦娃")

# 阻塞,等待分支线程结束
thread.join()
print("a=", a)
