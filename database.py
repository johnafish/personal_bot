""" Local Database to Store Growth Information """
import sqlite3

class Database:
    """ Database class """
    def __init__(self):
        """ Initialize db from file """
        self.database_file = "database.sqlite"
        self.connection = sqlite3.connect(self.database_file)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """ Create table in db """
        column_string = ""
        for column in columns:
            column_string += "{0} {1},".format(column["name"], column["type"])
        column_string = column_string[:-1]
        self.cursor.execute("CREATE TABLE {0} ({1})".format(table_name, column_string))
        self.connection.commit()

    def add_column(self, table_name, column_name, column_type):
        """ Add column to db """
        self.cursor.execute("ALTER TABLE {0} ADD COLUMN '{1}' {2}"\
                            .format(table_name, column_name, column_type))
        self.connection.commit()

    def close(self):
        """ Close db connection """
        self.connection.close()
