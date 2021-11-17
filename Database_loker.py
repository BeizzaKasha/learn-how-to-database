import asyncio
import threading
import time

import database_user


class database_locker(database_user.Database_user):
    def __init__(self):
        super(database_locker, self).__init__()
        self.lock = threading.Lock()
        self.semi = threading.Semaphore(10)

    def get_value(self, key):
        while self.lock.locked():
            time.sleep(0.0001)
        self.semi.acquire()
        # print("-----------------------reading------------------------")
        # print("inside lock of read")
        val = super(database_locker, self).get_value(key)
        # print("getting out lock of read")
        # print("--------------------stop-reading----------------------")
        self.semi.release()
        return val

    def set_value(self, key, val):
        self.lock.acquire()
        # print("+++++++++++++++++++++++++writing++++++++++++++++++++++")
        # print("inside lock of write")
        val = super(database_locker, self).set_value(key, val)
        # print("getting out lock of write")
        # print("+++++++++++++++++++++stop+writing+++++++++++++++++++++")
        self.lock.release()
        return val

    def delete_value(self, key):
        self.lock.acquire()
        # print("inside lock of delete")
        val = super(database_locker, self).delete_value(key)
        # print("getting out lock of delete")
        self.lock.release()
        return val


def main():
    dita = database_locker()
    threds = []
    for i in range(10):
        t = threading.Thread(target=dita.set_value("hello" + str(i), "mylife"))
        threds.append(t)
        t.start()
        t = threading.Thread(target=dita.get_value("hello" + str(i),))
        threds.append(t)
        t.start()
        t = threading.Thread(target=dita.delete_value("hello" + str(i)))
        threds.append(t)
        t.start()
        print("--------------")


if __name__ == "__main__":
    main()
