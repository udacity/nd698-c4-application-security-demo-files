import sqlite3
import psycopg2
import random
import string

class Conn_postgres():
    conn = None
    cursor = None

    def __init__(self):
        self.open()

    def open(self):
        self.conn = psycopg2.connect(user = "vulnwebsiteuser",
                                    password = "weakpasswordrule",
                                    host = "localhost",
                                    port = "5432",
                                    database = "vulnwebsite")
        self.cursor = self.conn.cursor()
        print("Postgres Connection Open")

    def close(self):
        self.conn.close()
        print("Postgres Connection Closed")

    def isclosed(self):
        try:
            resultset = self.conn.closed
            if resultset == 1:
                return True
            else:
                return False
        except:
            return True

    def createTable(self, tablename, query):
        self.cursor.execute("DROP TABLE IF EXISTS " + tablename + "; " + query)
        self.conn.commit()
        print("Postgres Table " + tablename + " Created")

    def randPassword(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def setup(self):
        if self.isclosed():
            self.open()
            
        self.createTable('users', 'CREATE TABLE users (id SERIAL PRIMARY KEY, role TEXT NOT NULL, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO users (role, firstname, lastname, username, password) VALUES ('admin','flag','flag{548562}','admin',MD5('" + self.randPassword(16) + "'));")
        self.cursor.execute("INSERT INTO users (role, firstname, lastname, username, password) VALUES ('user','john','doe','jdoe','5f4dcc3b5aa765d61d8327deb882cf99');")
        self.conn.commit()
        print("Postgres Table users Data Added")

        self.createTable('users2', 'CREATE TABLE users2 (id SERIAL PRIMARY KEY, role TEXT NOT NULL, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO users2 (role, firstname, lastname, username, password) VALUES ('admin','test','test','test', '839f508bf5ea5849ea4d09c74792d44e');")
        self.cursor.execute("INSERT INTO users2 (role, firstname, lastname, username, password) VALUES ('user','user','user','user', 'cb966b2a71ad4aa43b9b6dc9d93b673c');")
        self.conn.commit()
        print("Postgres Table users2 Data Added")

        self.createTable('customers', 'CREATE TABLE customers (id SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('paul','doe','pdoe','d8578edf8458ce06fbc5bb76a58c5ca4');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('john','doe','jdoe','e68e11be8b70e435c65aef8ba9798ff7775c361e');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('dave','doe','ddoe','b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('mike','doe','mdoe','8621ffdbc5698829397d97767ac13db3');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('nick','doe','ndoe','df53ca268240ca76670c8566ee54568a');")
        self.conn.commit()
        print("Postgres Table customers Data Added")

        self.createTable('secrets', 'CREATE TABLE secrets (id SERIAL PRIMARY KEY, supersecretstuff TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO secrets (supersecretstuff) VALUES ('flag{415462}');")
        self.conn.commit()
        print("Postgres Table secrets Data Added")

        self.createTable('messages', 'CREATE TABLE messages (id SERIAL PRIMARY KEY, chat_id SERIAL, user_id SERIAL, body TEXT);')
        self.cursor.execute("INSERT INTO messages (chat_id, user_id, body) VALUES (1,1,' Welcome to our site, how do you like our chat service. Still a work in progress.');")
        self.cursor.execute("INSERT INTO messages (chat_id, user_id, body) VALUES (2,1,' Welcome to our site, how do you like our new chat service. Fix some bugs but still a work in progress.');")
        self.conn.commit()
        print("Postgres Table messages Data Added")

        self.close()

    def insert(self, query):
        if self.isclosed():
            self.open()

        print("Postgres Insert:" + query)
        self.cursor.execute(query)
        self.conn.commit()

    def exec(self, query):
        if self.isclosed():
            self.open()

        print("Postgres Exec:" + query)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
        