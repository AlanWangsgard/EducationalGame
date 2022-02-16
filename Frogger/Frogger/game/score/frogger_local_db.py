import sqlite3

class FroggerLocalDB:
    
    def __init__(self) -> None:
        self.connection = self.connect()

    def initializeDB(self):
        try:
            self.create_tables()
            print('Database created successfully!')
        except:
            print('Something went wrong while creating the database.')


    def create_tables(self):
        cur = self.connection.cursor()

        # Create table
        cur.execute(f'''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name text NOT NULL);
            ''')

        cur.execute(f'''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE ON UPDATE NO ACTION);
            ''')
        cur.execute(f'''
        CREATE TABLE IF NOT EXISTS game_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            level INTEGER,
            score INTEGER,
            lives INTEGER,
            date DATETIME,
            FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE ON UPDATE NO ACTION);
            ''')

    def connect(self):
        con = sqlite3.connect('scores.db')
        return con
