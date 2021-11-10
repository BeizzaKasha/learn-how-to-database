import threading
import Database_loker
import time
import random
from database_cons import *


class worker():
    def __init__(self):
        self.d = Database_loker.database_locker()

    def write(self, key, value):
        for i in range(20):
            self.d.set_value(key + str(i), value)
            # time.sleep(0.0001)

    def read(self, num):
        for i in range(1):
            for key in self.d.data:
                print("read" + num + "." + str(i) + ": " + key + "=>" + self.d.get_value(key))  # + "\n"
        # print("finito read\n\n\n")

    def delete(self, key):
        for i in range(9):
            self.d.delete_value(key + str(i))
            # time.sleep(0.0001)


def main():
    worker_obj = worker()
    threds = []
    for i in range(2):
        threds.append(threading.Thread(target=worker_obj.write, args=("hello" + str(i) + ".", "mylife")))
        # threds.append(threading.Thread(target=worker_obj.delete, args=("hello" + str(i) + "."), ))
        threds.append(threading.Thread(target=worker_obj.read, args=str(i)))
    for t in threds:
        t.start()
    for t in threds:
        while t.is_alive():
            pass
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
