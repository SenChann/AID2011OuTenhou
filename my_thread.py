"""
自定义线程类
"""
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, song):
        self.song = song
        super().__init__()  # 得到父类内容

    # 线程要做的事情
    def run(self):
        for i in range(3):
            sleep(2)
            print("播放：", self.song)


mt = MyThread("WTF")
mt.start()
