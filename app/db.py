import sqlite3


class webBlock_db:

    def __init__(self):
        self.website_www = 'website_www'
        self.website_http = 'website_http'

    def show_all_blockes(self):
        self.conn = sqlite3.connect('blocks.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT rowid, * FROM blocks")
        items = self.cur.fetchall()

        for item in items:
            print(item)

        self.conn.commit()
        self.conn.close()
        return item

    def create_table(self):
        self.conn = sqlite3.connect('blocks.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            http TEXT,
            www TEXT
        )""")
        self.conn.commit()
        self.conn.close()

    def add_one(self, website_www, website_http):
        self.conn = sqlite3.connect('blocks.db')
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO blocks VALUES (NULL,?,?)", (website_http, website_www))
        self.conn.commit()
        self.conn.close()

    def delete_one(self, id):
        self.conn = sqlite3.connect('blocks.db')
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM blocks WHERE id = (?)", id)
        self.conn.commit()
        self.conn.close()
