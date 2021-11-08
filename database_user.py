from io import open
import os
import database
import pickle
from database_cons import *


class Database_user(database.Database):
    def __init__(self):
        try:
            dbfile = open('pikel.txt', 'rb')
            db = pickle.load(dbfile)
            super(Database_user, self).__init__(db)
        except:
            super(Database_user, self).__init__({})

    def get_value(self, key):
        return super(Database_user, self).get_value(key)

    def set_value(self, key, val):
        """
        :param key:
        :param val:
        :return: 0 if successful, 1 if
        """
        retval = super(Database_user, self).set_value(key, val)
        if retval == Database_cons.SUCCESSFUL:
            try:
                dbfile = open("pikel.txt", "wb")
                pickle.dump(self.data, dbfile)
                dbfile.close()
                return retval
            except:
                return Database_cons.FILE_ERROR
        else:
            return retval

    def delete_value(self, key):
        """
        :param key: the key the user wnat to delete
        :return: 0 if successful and 1 if unsuccessful
        """
        val = super(Database_user, self).delete_value(key)
        if val != Database_cons.KEY_NOT_FOUND:
            try:
                dbfile = open("pikel.txt", "wb")
                pickle.dump(self.data, dbfile)
                dbfile.close()
            except:
                return Database_cons.FILE_ERROR
        return val


def main():
    dita = Database_user()
    print(dita.get_value(input()))

    for i in range(1):
        mykey = input("key: ")
        mydata = input("data: ")
        dita.set_value(mykey, mydata)

        mykey = input("key to delete: ")
        dita.delete_value(mykey)

    print(dita.get_value(input()))


if __name__ == "__main__":
    main()
