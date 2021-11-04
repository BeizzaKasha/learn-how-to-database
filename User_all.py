import threading
import Database_loker
import time
import random


class worker(Database_loker.database_locker):
    def __init__(self):
        super(worker, self).__init__()

    def writer(self, key, value):
        for i in range(20):
            super(worker, self).writing(key + str(i), value)
            time.sleep(0.0001)

    def reader(self):
        for i in range(4):
            super(worker, self).reading()

    def deleter(self, key):
        for i in range(9):
            super(worker, self).deleting(key + str(i))
            time.sleep(0.0001)


def main():
    workers = worker()
    threds = []
    for i in range(1):
        # threds.append(threading.Thread(target=workers.writer, args=("hello" + str(i), "mylife")))
        # threds.append(threading.Thread(target=workers.deleter, args=("hello" + str(i), )))
        threds.append(threading.Thread(target=workers.reader))
    for t in threds:
        t.start()
    print("--------------")


if __name__ == "__main__":
    main()
