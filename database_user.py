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
            """
                if the file is empty, put null key in it
            """
            self.write("null", "null")

    def write(self, key, value):
        if value != "":
            super().set_value(key, value)
            dbfile = open("examplePickle", "wb")
            pickle.dump(self.data, dbfile)
            dbfile.close()
            """
                if there's a null key, delete it
            """
        if super().delete_value("null"):
            self.delete("null")

    def delete(self, key):
        """
        :param key: the key the user wnat to delete
        :return: 0 if successful and 1 if unsuccessful
        """
        data = super().delete_value(key)
        dbfile = open("examplePickle", "wb")
        pickle.dump(self.data, dbfile)
        dbfile.close()
        if data is not None:
            return 0
        else:
            return 1


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
