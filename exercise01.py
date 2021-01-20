"""
练习01：
    现在有500张票，存到一个列表中["T1",..."T500"]
    10个窗口同时卖这500张票，记为W1-W10

    使用10个线程模拟这10个窗口，同时卖票，直到所有的票都卖出为止，每出一张票需要0.1秒
    print("W1---T250")
"""

from threading import Thread
from time import sleep
import random

# 准备好票
# ticket = []
# for i in range(1, 501):
#     ticket.append("T%d" % i)
ticket = ["T%d" % i for i in range(1, 501)]


def sell(i):
    while ticket:
        print("W%d--%s" % (i, ticket.pop(0)))
        sleep(0.1)


for i in range(1, 11):
    t = Thread(target=sell, args=(i,))
    t.start()
