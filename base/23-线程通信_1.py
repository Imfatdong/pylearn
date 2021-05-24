import time
from threading import Barrier, Semaphore, current_thread, Thread, BoundedSemaphore, Timer, local, Event
import random

barrier = Barrier(5)
semaphore = Semaphore(5)
boundedSemaphore = BoundedSemaphore(5)
thread_local = local()


def test_barrier():
    def run():
        print("%s is running" % (current_thread().getName(),))
        barrier.wait()
        print("%s is resume" % (current_thread().getName(),))

    for i in range(10):
        Thread(target=run).start()


def test_semaphore():
    def run():
        semaphore.acquire()
        # semaphore.release()  #可以无限释放，可以超出初始信号量的值，可以通过BoundedSemaphore替换
        print("%s 占用一个信号量 ,剩余信号量 %s" % (current_thread().getName(), semaphore._value))
        time.sleep(random.choice([1, 2, 3, 4]))
        semaphore.release()
        print("%s release ,剩余信号量 %s" % (current_thread().getName(), semaphore._value))

    for i in range(10):
        Thread(target=run).start()


def test_bounded_semaphore():
    def run():
        # boundedSemaphore.release()  #不可以无限释放 ValueError: Semaphore released too many times
        boundedSemaphore.acquire()
        print("%s 占用一个信号量 ,剩余信号量 %s" % (current_thread().getName(), boundedSemaphore._value))
        time.sleep(random.choice([1, 2, 3, 4]))
        boundedSemaphore.release()
        print("%s release ,剩余信号量 %s" % (current_thread().getName(), boundedSemaphore._value))

    for i in range(10):
        Thread(target=run).start()


def test_timer():
    """
    延迟执行
    :return:
    """

    def run():
        print('timer start...')
        time.sleep(2)
        print('timer end...')

    timer = Timer(5, run)
    timer.start()


def test_thread_local():
    def run(i):
        thread_local.x = 1000  # 必须先赋值
        for j in range(10000):
            thread_local.x += i
            thread_local.x -= i
        print("%s thread_local的最终值 %d" % (current_thread().getName(), thread_local.x))

    for i in range(10):
        Thread(target=run, args=(i,)).start()


event = Event()


def test_event():
    """
    通过event进行线程之间的通讯

    Event（事件）是最简单的线程通信机制之一：
    一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，
    当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。
    :return:
    """

    def run1():
        print("%s 等待事件中" % (current_thread().getName(),))
        event.wait()
        event.clear()  # 重置状态
        print("%s 事件到达，唤醒" % (current_thread().getName(),))

    def run2():
        time.sleep(2)
        print("%s 发送事件" % (current_thread().getName(),))
        event.set()

    Thread(target=run1).start()
    Thread(target=run2).start()
    pass


def main():
    # test_barrier()
    # test_semaphore()
    # test_bounded_semaphore()
    # test_timer()
    # test_thread_local()
    test_event()


if __name__ == '__main__':
    main()
