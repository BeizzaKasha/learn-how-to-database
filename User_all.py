import threading
import Database_loker
import time
import random


class worker(Database_loker.database_locker):
    def __init__(self):
        super().__init__()

    def writer(self, key, value):
        for i in range(10):
            super().write(key + str(i), value)
            # time.sleep(0.0001)

    def reader(self):
        for i in range(5):
            super().read()

    def deleter(self, key):
        for i in range(9):
            super().delete(key + str(i))
            # time.sleep(0.0001)


def main():
    workers = worker()
    threds = []
    for i in range(10):
        threds.append(threading.Thread(target=workers.writer, args=("hello" + str(i), "mylife")))
        threds.append(threading.Thread(target=workers.deleter, args=("hello" + str(i))))
        threds.append(threading.Thread(target=workers.reader))
    for t in threds:
        t.start()
    print("--------------")
    workers.read()


if __name__ == "__main__":
    main()
