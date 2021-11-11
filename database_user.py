from io import open
import database
import pickle
from database_cons import *


class Database_user(database.Database):
    def __init__(self):
        try:  # try to load existing data if there is any, if there isn't create an empty dictionary
            dbfile = open('pikel.txt', 'rb')
            db = pickle.load(dbfile)
            super(Database_user, self).__init__(db)
        except:
            super(Database_user, self).__init__({})

    def get_value(self, key):
        """
        :param key: key to read from
        :return: value of key if successful or KEY_NOT_FOUND if unsuccessful
        """
        return super(Database_user, self).get_value(key)

    def set_value(self, key, val):
        """
        :param key: key to write into
        :param val: what to write in the key
        :return: SUCCESSFUL if successful,
            FILE_ERROR if there was a problem with writing in the file,
            and DICTIONARY_ERROR if there was a problem with the database writing.
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
        :param key: the key the user want to delete
        :return: value that got deleted if successful,
            FILE_ERROR if there was a problem with the file key deleting,
            KEY_NOT_FOUND if there was a problem with the database deleting.
        """
        val = super(Database_user, self).delete_value(key)
        if val != Database_cons.KEY_NOT_FOUND:
            try:
                dbfile = open("pikel.txt", "wb")
                pickle.dump(self.data, dbfile)
                dbfile.close()
            except:
                val = Database_cons.FILE_ERROR
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
