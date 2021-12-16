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
        self.cursor.execute("INSERT INTO users (role, firstname, lastname, username, password) VALUES ('user','john','doe','johndoe','MySecurePassword');")
        self.cursor.execute("INSERT INTO users (role, firstname, lastname, username, password) VALUES ('user','paul','doe','pauldoe','BadPassword');")
        self.cursor.execute("INSERT INTO users (role, firstname, lastname, username, password) VALUES ('user','steve','doe','stevedoe','NotSecurePassword');")
        self.conn.commit()
        print("Postgres Table users Data Added")

        self.createTable('userlist', 'CREATE TABLE userlist (id SERIAL PRIMARY KEY, role TEXT NOT NULL, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO userlist (role, firstname, lastname, username, password) VALUES ('admin','admin','admin','admin', '5421548754');")
        self.cursor.execute("INSERT INTO userlist (role, firstname, lastname, username, password) VALUES ('user','john','doe','johndoe', '1265412578');")
        self.cursor.execute("INSERT INTO userlist (role, firstname, lastname, username, password) VALUES ('user','paul','doe','pauldoe', '3256523652');")
        self.cursor.execute("INSERT INTO userlist (role, firstname, lastname, username, password) VALUES ('user','steve','doe','stevedoe', 'flag{548562}');")
        self.conn.commit()
        print("Postgres Table userlist Data Added")

        self.createTable('messages', 'CREATE TABLE messages (id SERIAL PRIMARY KEY, chat_id SERIAL, user_id SERIAL, body TEXT);')
        self.cursor.execute("INSERT INTO messages (chat_id, user_id, body) VALUES (1,1,' Welcome to our site, how do you like our chat service?');")
        self.conn.commit()
        print("Postgres Table messages Data Added")

        #self.createTable('friendlist', 'CREATE TABLE friendlist (id SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT NOT NULL, password TEXT NOT NULL);')
        self.createTable('friendlist', 'CREATE TABLE friendlist (id SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT, password TEXT NOT NULL, email TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO friendlist (firstname, lastname, email, password) VALUES ('john','doe','johndoe@example.com','34819d7beeabb9260a5c854bc85b3e44');")
        self.cursor.execute("INSERT INTO friendlist (firstname, lastname, email, password) VALUES ('paul','doe','pauldoe@example.com','d8578edf8458ce06fbc5bb76a58c5ca4');")
        self.cursor.execute("INSERT INTO friendlist (firstname, lastname, email, password) VALUES ('steve','doe','stevedoe@example.com','76419c58730d9f35de7ac538c2fd6737');")
        self.conn.commit()
        print("Postgres Table friendlist Data Added")

        self.createTable('customers', 'CREATE TABLE customers (id SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('paul','doe','pdoe','5f4dcc3b5aa765d61d8327deb882cf99');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('john','doe','jdoe','276f8db0b86edaa7fc805516c852c889');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('dave','doe','ddoe','08f90c1a417155361a5c4b8d297e0d78');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('mike','doe','mdoe','7b7a53e239400a13bd6be6c91c4f6c4e');")
        self.cursor.execute("INSERT INTO customers (firstname, lastname, username, password) VALUES ('nick','doe','ndoe','6a204bd89f3c8348afd5c77c717a097a');")
        self.conn.commit()
        print("Postgres Table customers Data Added")

        self.createTable('users2', 'CREATE TABLE users2 (id SERIAL PRIMARY KEY, role TEXT NOT NULL, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO users2 (role, firstname, lastname, username, password) VALUES ('admin','test','test','test', '839f508bf5ea5849ea4d09c74792d44e');")
        self.cursor.execute("INSERT INTO users2 (role, firstname, lastname, username, password) VALUES ('user','user','user','user', 'cb966b2a71ad4aa43b9b6dc9d93b673c');")
        self.conn.commit()
        print("Postgres Table users2 Data Added")


        self.createTable('weakhash', 'CREATE TABLE weakhash (id SERIAL PRIMARY KEY, weakhashes TEXT NOT NULL);')
        self.cursor.execute("INSERT INTO weakhash (weakhashes) VALUES ('25d55ad283aa400af464c76d713c07ad');")
        self.cursor.execute("INSERT INTO weakhash (weakhashes) VALUES ('7c222fb2927d828af22f592134e8932480637c0d');")
        self.cursor.execute("INSERT INTO weakhash (weakhashes) VALUES ('9f18b4c3223da0db16ad524100d32576:pZ`');")
        self.conn.commit()
        print("Postgres Table weakhash Data Added")

        self.createTable('hashes', 'CREATE TABLE hashes (id SERIAL PRIMARY KEY, hash TEXT);')
        self.cursor.execute("INSERT INTO hashes (hash) VALUES ('d8578edf8458ce06fbc5bb76a58c5ca4');")
        self.cursor.execute("INSERT INTO hashes (hash) VALUES ('e68e11be8b70e435c65aef8ba9798ff7775c361e');")
        self.cursor.execute("INSERT INTO hashes (hash) VALUES ('b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3');")
        self.cursor.execute("INSERT INTO hashes (hash) VALUES ('8621ffdbc5698829397d97767ac13db3');")
        self.cursor.execute("INSERT INTO hashes (hash) VALUES ('df53ca268240ca76670c8566ee54568a');")
        self.conn.commit()
        print("Postgres Table hashes Data Added")


        self.close()

    def insert(self, query):
        if self.isclosed():
            self.open()

        print("Postgres Insert:" + query)
        self.cursor.execute(query)
        self.conn.commit()

    def insert_safe(self, query, data):
        if self.isclosed():
            self.open()

        print("Postgres Insert:" + query)
        self.cursor.execute(query, data)
        self.conn.commit()

    def exec(self, query):
        if self.isclosed():
            self.open()

        print("Postgres Exec:" + query)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
        
    def exec_safe(self, query, data):
        if self.isclosed():
            self.open()

        print("Postgres Exec:" + query)
        self.cursor.execute(query, data)

        data = self.cursor.fetchall()
        return data