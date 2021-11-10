import threading
import database_user


class database_locker(database_user.Database_user):
    def __init__(self):
        super(database_locker, self).__init__()
        self.lock = threading.Lock()

    def get_value(self, key):
        self.lock.acquire()
        val = super(database_locker, self).get_value(key)
        self.lock.release()
        return val

    def set_value(self, key, val):
        self.lock.acquire()
        super(database_locker, self).set_value(key, val)
        self.lock.release()

    def delete_value(self, key):
        self.lock.acquire()
        super(database_locker, self).delete_value(key)
        self.lock.release()


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
