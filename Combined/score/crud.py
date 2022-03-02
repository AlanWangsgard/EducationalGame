import sqlite3
from game.constants import DB_PATH

class CrudDB:
    def __init__(self, table) -> None:
        self.connection = None
        self.table = table

    def connect(self):
        self.connection = sqlite3.connect(DB_PATH)

    def insert(self, fields, values, query = None):
        self.connect()
        cur = self.connection.cursor()
        cur.execute(query if query is not None else f"INSERT INTO {self.table} {fields} VALUES {values}")
        self.connection.commit()
        self.connection.close()

    def update(self, id = None, field = None, value = None, query = None):
        if query is None and (id is None or field is None or value is None): 
            print('Invalid input. If a query is not provided, id, field, and value are required.')
            return 
        self.connect()
        cur = self.connection.cursor()
        cur.execute(query if query is not None else f"UPDATE {self.table} SET {field} = {value} WHERE id = {id}")
        self.connection.commit()
        self.connection.close()

    def list(self, query = None):
        self.connect()
        cur = self.connection.cursor()
        rows = cur.execute(query if query is not None else f"SELECT * FROM {self.table}").fetchall()
        self.connection.close()
        return rows

    def getById(self, id:int = None, query = None):
        try:
            print(query)
            self.connect()
            cur = self.connection.cursor()
            rows = cur.execute(query if query is not None else f"SELECT * FROM {self.table} WHERE id = {id}").fetchall()
            print(rows)
            self.connection.close()
            return rows[0]
        except:
            return None

    def getByField(self, field, value):
        try:
            print(field, value)
            self.connect()
            cur = self.connection.cursor()
            rows = cur.execute(f"SELECT * FROM {self.table} WHERE {field} = {value}").fetchall()
            print(rows)
            self.connection.close()
            return rows[0]
        except:
            return None