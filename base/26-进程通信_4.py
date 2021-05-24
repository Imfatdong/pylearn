import random
import threading, time, queue

"""

生产者消费者模型，利用condition完成

"""


def producer(q: queue.Queue, condition: threading.Condition, name: str):
    while True:
        value = chr(random.randint(65, 90))
        with condition:
            if not q.full():
                print("%s生产了 %s" % (name, value))
                q.put(value)
                condition.notify_all()
                time.sleep(random.choice([1]))
            else:
                condition.wait()


def consumer(q: queue.Queue, condition: threading.Condition, name: str):
    while True:
        with condition:
            if not q.empty():
                value = q.get()
                print("%s消费了 %s" % (name, value))
                condition.notify_all()
            else:
                condition.wait()
def main():
    q = queue.Queue(5)
    condition = threading.Condition()
    # threading.Thread(target=producer, args=(q, condition, "生产者" + str(0 + 1))).start()
    # threading.Thread(target=consumer, args=(q, condition, "消费者" + str(0 + 1))).start()

    for i in range(5):
        threading.Thread(target=producer, args=(q, condition, "生产者" + str(i + 1))).start()
    for i in range(10):
        threading.Thread(target=consumer, args=(q, condition, "消费者" + str(i + 1))).start()

    pass

if __name__ == '__main__':
    main()