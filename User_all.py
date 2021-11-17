import threading
import Database_loker
import time
import random
from database_cons import *


class worker():
    def __init__(self):
        self.d = Database_loker.database_locker()

    def read(self, num):
        for i in range(30):
            key = "hello" + num + "." + str(i)
            print(key + "=>" + self.d.get_value(key))  # + "\n"

    def write(self, key, value):
        for i in range(30, 0, -1):
            print(f"worker.write: {self.d.set_value(key + str(i - 1), value)}")

    def delete(self, key):
        for i in range(29):
            print(f"worker.delete: {self.d.delete_value(key + str(i))}")


def main():
    worker_obj = worker()
    threds = []
    for i in range(5):
        threds.append(threading.Thread(target=worker_obj.write, args=("hello" + str(i) + ".", "mylife",)))
        threds.append(threading.Thread(target=worker_obj.delete, args=("hello" + str(i) + ".",)))
        threds.append(threading.Thread(target=worker_obj.read, args=str(i), ))
    for t in threds:
        t.start()
    for t in threds:
        while t.is_alive():
            pass
    """deleters = []  # for cleaner data in the end
    for i in range(5):
        deleters.append(threading.Thread(target=worker_obj.delete, args=("hello" + str(i) + ".",)))
    for t in deleters:
        t.start()
    for t in threds:
        while t.is_alive():
            pass"""
    print("----------------------------------------------------------------------------------------------------"
          "---------------------------------------------------")
    for key in worker_obj.d.data:
        print(key + "=>" + worker_obj.d.get_value(key))


if __name__ == "__main__":
    main()
