from multiprocessing import Process, Queue
import os
import time
import random

# 进程之间通过队列通信



def read(q: Queue):
    print("读进程开始 id为 %s" %(os.getpid(),))
    while True:
        print("读取的数据为：%s " % (q.get(),))


def write(q: Queue):
    print("写进程开始 id为 %s" % (os.getpid(),))
    for i in "ABCDEFG":
        q.put(i)
        time.sleep(random.choice([1, 2, 3]))


def main():
    q = Queue()
    read_thread = Process(target=read, args=(q,))
    write_thread = Process(target=write, args=(q, ))

    read_thread.start()
    write_thread.start()
    read_thread.join()
    write_thread.join()

if __name__ == '__main__':
    main()


