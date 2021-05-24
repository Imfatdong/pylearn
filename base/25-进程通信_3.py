import time
from threading import Thread
import queue
import random


"""
生产者消费者模型
"""


def producer(q: queue.Queue ,name:str):

    while True:
        value = chr(random.randint(65, 90))
        print("%s生产了 %s" % (name, value))
        q.put(value)
        time.sleep(random.choice([1, 2, 3]))


def consumer(q: queue.Queue,name:str):
    while True:
        try:
            value = q.get(timeout=5)
            print("%s消费了 %s" % (name, value))
        except queue.Empty:
            print("%s提示消费完了" % (name,))


def main():
    q = queue.Queue()
    for i in range(5):
        Thread(target=producer, args=(q,"生产者"+str(i+1) )).start()
    for i in range(10):
        Thread(target=consumer, args=(q,"消费者"+str(i+1))).start()


if __name__ == '__main__':
    main()
