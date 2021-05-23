import time
from threading import Barrier, Semaphore, current_thread, Thread, BoundedSemaphore, Timer, local
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


def main():
    # test_barrier()
    # test_semaphore()
    # test_bounded_semaphore()
    # test_timer()
    test_thread_local()


if __name__ == '__main__':
    main()
