from database_cons import *


class Database:
    def __init__(self, db):
        self.data = db

    def set_value(self, key, val):
        """
        :param key: key to write into
        :param val: value to write
        :return: SUCCESSFUL if successful and DICTIONARY_ERROR if unsuccessful
        """
        try:
            if val != "":  # if val is empty don't write at all
                self.data[key] = val
                return Database_cons.SUCCESSFUL
        except:
            pass

        return Database_cons.DICTIONARY_ERROR

    def get_value(self, key):
        """
        :param key: key to read from
        :return: value of key if successful or KEY_NOT_FOUND if unsuccessful
        """
        if key in self.data:
            return self.data[key]
        else:
            return Database_cons.KEY_NOT_FOUND

    def delete_value(self, key):
        """
        :param key: key to delete
        :return: value that got deleted if successful or KEY_NOT_FOUND if successful
        """
        if key in self.data:
            val = self.data[key]
            self.data.pop(key)
            return val
        return Database_cons.KEY_NOT_FOUND
