from threading import Thread, Lock, current_thread
from time import sleep

lock = Lock()


# 线程之间通过全局变量共享数据

class My_thread(Thread):

    def __init__(self, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name = name

    def run(self):
        print("线程名称 %s" % (self.__name,));


count = 1000


def run(c: int):
    global count, lock
    for i in range(1000000):
        try:
            lock.acquire()  # 加锁保证安全
            count += c
            count -= c
        finally:
            lock.release()

        # 不用try finally的高级写法
        # with lock:
        #     pass

    print("count 的值", count)


def create_thread():
    t = Thread(target=run, args=(1,))
    t.setDaemon(True)
    t.start()
    t2 = My_thread(name="继承")
    t2.start()

    t.join()

    while True:
        print("主线程....")
        sleep(2)


def thread_unsafe():
    t1 = Thread(target=run, args=(1,))
    t2 = Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("count 的最终值", count)


def main():
    print("当前线程名称", current_thread().getName())
    thread_unsafe()
    create_thread()


count = 0

if __name__ == '__main__':
    main()
