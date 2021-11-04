import threading
import database_user


class database_locker(database_user.Database_user):
    def __init__(self):
        super(database_locker, self).__init__()
        self.lokk = threading.Lock()
        self.state = "N"

    def reading(self):
        val = None
        """ while self.state == "W":
            pass"""
        self.lokk.acquire()

        # self.state = "R"
        for key in self.data:
            val = super(database_locker, self).read(key)
        # self.state = "N"
        self.lokk.release()

        return val

    def writing(self, key, value):
        """ while self.state == "N":
             pass"""
        self.lokk.acquire()
        # self.state = "W"
        super(database_locker, self).write(key, value)
        # self.state = "N"
        self.lokk.release()

    def deleting(self, key):
        """while self.state == "N":
            pass"""
        self.lokk.acquire()
        # self.state = "W"
        super(database_locker, self).delete(key)
        # self.state = "N"
        self.lokk.release()
        print(self.data)


def main():
    dita = database_locker()
    threds = []
    for i in range(10):
        t = threading.Thread(target=dita.write("hello" + str(i), "mylife"))
        threds.append(t)
        t.start()
        t = threading.Thread(target=dita.read())
        threds.append(t)
        t.start()
        t = threading.Thread(target=dita.delete("hello" + str(i)))
        threds.append(t)
        t.start()
        print("--------------")
    dita.read()


if __name__ == "__main__":
    main()
