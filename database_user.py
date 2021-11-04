from io import open
import os
import database
import pickle


class Database_user(database.Database):
    def __init__(self):
        super(Database_user, self).__init__()
        dbfile = open('pikel.txt', 'rb')
        db = pickle.load(dbfile)
        if db is not None:
            # print(self.data)
            for keys in db:
                self.set_value(keys, db[keys])
                print(keys, '=>', db[keys])
        dbfile.close()

    def read(self, key):
        return super(Database_user, self).get_value(key)

    def write(self, key, value):
        if value != "":
            super(Database_user, self).set_value(key, value)
            dbfile = open("pikel.txt", "wb")
            pickle.dump(self.data, dbfile)
            dbfile.close()
            # print(self.data)

    def delete(self, key):
        """
        :param key: the key the user wnat to delete
        :return: 0 if successful and 1 if unsuccessful
        """
        val = super(Database_user, self).delete_value(key)
        dbfile = open("pikel.txt", "wb")
        pickle.dump(self.data, dbfile)
        dbfile.close()
        if val is not None:
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
