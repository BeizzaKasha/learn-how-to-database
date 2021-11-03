import threading
import database_user


class database_locker(database_user.Database_user):
    def __init__(self):
        super().__init__()
        self.data = super().read()
        self.lokk = threading.Lock()
        self.state = "N"

    def read(self):
        if not self.state == "W" or not self.state == "D":
            super().read()

    def write(self, key, value):
        if not self.state == "W" or not self.state == "D":
            if not self.lokk.locked():
                self.lokk.acquire()
                self.state = "W"
                super().write(key, value)
                self.state = "N"
                self.lokk.release()

    def delete(self, key):
        if not self.state == "W" or not self.state == "D":
            if not self.lokk.locked():
                self.lokk.acquire()
                self.state = "D"
                super().delete(key)
                self.state = "N"
                self.lokk.release()


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
