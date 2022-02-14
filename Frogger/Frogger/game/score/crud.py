import sqlite3

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

    def update(self, id, field, value):
        self.connect()
        cur = self.connection.cursor()
        cur.execute(f"UPDATE {self.table} SET {field} = {value} WHERE id = {id}")
        self.connection.commit()
        self.connection.close()

    def list(self, query = None):
        self.connect()
        cur = self.connection.cursor()
        rows = cur.execute(query if query is not None else f"SELECT * FROM {self.table}").fetchall()
        self.connection.close()
        return rows

    def getById(self, id):
        try:
            self.connect()
            cur = self.connection.cursor()
            rows = cur.execute(f"SELECT * FROM {self.table} WHERE id = {id}").fetchall()
            self.connection.close()
            return rows[0]
        except:
            return None