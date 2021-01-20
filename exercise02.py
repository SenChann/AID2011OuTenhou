"""
练习02：
    使用两个分支线程，一个线程打印1-52 这52个数字
    另一个线程打印A-Z 这26个字母
    要求同时执行两个线程，打印顺序为
    12A34B...5152Z
"""
from threading import Thread, Lock
from time import sleep

lock_one = Lock()
lock_two = Lock()


def number():
    for i in range(1, 53, 2):
        lock_one.acquire()
        print(i)
        print(i + 1)
        lock_two.release()


# 打印A-Z
lock_two.acquire()
def letter():
    for i in range(65, 91):
        lock_two.acquire()
        print(chr(i))
        lock_one.release()


for item in [number, letter]:
    t = Thread(target=item)
    t.start()
