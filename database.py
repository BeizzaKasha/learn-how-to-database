from database_cons import *


class Database:
    def __init__(self, db):
        self.data = db

    def set_value(self, key, val):
        """
        sets the value for the specified key to the specified value
        returns 0 if successful and 1 if unsuccessful
        """
        try:
            if val != "":
                self.data[key] = val
                return Database_cons.SUCCESSFUL
        except:
            print("there was a problem in set_value")

        return Database_cons.DICTIONARY_ERROR

    def get_value(self, key):
        """
        :param key: key to read from data
        :return: value of key if successful or None if unsuccessful
        """
        if key in self.data:
            return self.data[key]
        else:
            return Database_cons.KEY_NOT_FOUND

    def delete_value(self, key):
        """
        :param key: key to delete
        :return: value that got deleted if successful or None if successful
        """
        if key in self.data:
            val = self.data[key]
            self.data.pop(key)
            return val
        return Database_cons.KEY_NOT_FOUND
