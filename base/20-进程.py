from multiprocessing import Process
from time import sleep
import os
from multiprocessing import Pool
import random


"""
进程之间不能直接通过共享变量通信
"""

def run():
    while True:
        print("子进程1 running")
        sleep(1)


class MyProcess(Process):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self) -> None:
        while True:
            print("子进程2 2s running")
            sleep(2)


def create_process1():
    """
    创建进程的方式一 通过Process
    :return:
    """
    p = Process(group=None, target=run, name=None, args=(), kwargs={})
    print(os.getpid())
    p.start()
    # p.join()
    # p.terminate()
    print(p.name)


def create_process2():
    """
    创建进程的方式二 继承自Process
    :return:
    """
    p = MyProcess()
    p.start()

def p():
    ran = random.choice([1, 2, 3, 4])
    sleep(ran)
    print("%s 随机休眠 %d s" % (os.getpid(), ran))
    # print(o)


def create_process3():
    """
    创建进程的方式三 通过进程池Pool
    :return:
    """
    pool = Pool(8)
    for i in range(10):
        pool.apply_async(p)
    pool.close()


if __name__ == '__main__':

    create_process1()
    create_process2()
    create_process3()
    while True:
        print("主进程 running")
        sleep(1)
