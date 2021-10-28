from io import open
import os
import database
import pickle


class Database_user(database.Database):
    def __init__(self):
        super().__init__()

    def read(self):
        if os.stat("examplePickle").st_size != 0:
            dbfile = open('examplePickle', 'rb')
            db = pickle.load(dbfile)
            for keys in db:
                super().set_value(keys, db[keys])
                print(keys, '=>', db[keys])
            dbfile.close()
        else:
            self.write(None, None)

    def write(self, key, value):
        super().set_value(key, value)
        dbfile = open("examplePickle", "wb")
        pickle.dump(self.data, dbfile)
        dbfile.close()

    def delete(self, key):
        # data = super().delete_value(key)לא נכון צריך לתקן
        # self.write(key, data)
        # print(self.data)


def main():
    dita = Database_user()
    dita.read()

    for i in range(1):
        mykey = input("key: ")
        mydata = input("data: ")
        dita.write(mykey, mydata)

        mykey = input("key to delete: ")
        dita.delete(mykey)

    dita.read()


if __name__ == "__main__":
    main()