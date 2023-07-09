import sqlite3
import datetime

class Database:
    def __init__(self, db_name='passwords.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS passwords (
            username TEXT PRIMARY KEY,
            password TEXT,
            ip_address TEXT,
            domain_name TEXT,
            creation_date TEXT
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_password(self, username, password, ip_address, domain_name):
        query = '''
        INSERT INTO passwords (username, password, ip_address, domain_name, creation_date)
        VALUES (?, ?, ?, ?, ?)
        '''
        creation_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.conn.execute(query, (username, password, ip_address, domain_name, creation_date))
        self.conn.commit()  

    def get_password(self, username):
        query = '''
        SELECT password FROM passwords WHERE username = ?
        '''
        cursor = self.conn.execute(query, (username,))
        password = cursor.fetchone()
        return password[0] if password else None
    
    def remove_password(self, username):
        query = '''
        DELETE FROM passwords WHERE username = ?
        '''
        self.conn.execute(query, (username,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()