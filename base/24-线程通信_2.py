"""

正常情况下线程的执行顺序是操作系统控制的，如果需要让我们自己来控制线程的执行顺序，需要用到Condition（条件变量）类。

尝试实现这么一个需求，有一个线程输出 0  2 4 6 8 ，另一个线程输出 1 3 5 7 9 ，
这两个线程并行执行时，显示的结果是混乱无序的，要求输出结果为0  1 2 3 4 5 6 7 8 9 。

Condition类的方法说明：

acquire([timeout])/release(): 调用关联的锁的相应方法。  　　

wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。  　　

notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。  　　

notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

condition同样可以使用with上下文管理器来自动管理锁。

练习：真实的场景中，生产者只有生成了东西，消费者才能消费。请使用Condition改进我们上面的生产者消费者模型。

"""

import threading, time

# 线程条件变量
cond = threading.Condition()


def run1():
    for i in range(0, 10, 2):
        # condition自带一把锁
        # 获取锁
        if cond.acquire():
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 当前线程执行完成，等待另一个线程执行，并释放锁
            cond.wait()
            # 通知另一个线程可以运行了。
            cond.notify()


def run2():
    for i in range(1, 10, 2):
        # 获取锁
        if cond.acquire():
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 通知上面的线程你不要等了，该走了。
            cond.notify()
            # 然后等待上一个线程给自己继续执行的信号。
            cond.wait()


if __name__ == '__main__':
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()
