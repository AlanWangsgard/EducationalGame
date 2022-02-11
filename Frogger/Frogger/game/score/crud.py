import sqlite3
from traceback import print_tb

class CrudDB:
    def __init__(self, table) -> None:
        self.connection = None
        self.table = table

    def connect(self):
        self.connection = sqlite3.connect('scores.db')

    def insert(self, fields, values):
        self.connect()
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO {self.table} {fields} VALUES {values}")
        self.connection.commit()
        self.connection.close()

    def list(self):
        self.connect()
        cur = self.connection.cursor()
        rows = cur.execute(f"SELECT * FROM {self.table}").fetchall()
        self.connection.close()
        return rows