def doLogin(username, password):
    if username == 'root':
        if password == 'root':
            print("OK, logged in")
        else:
            print("Sorry your password is incorrect")
    else:
        if password == 'password':
            print("OK, logged in")
        else:
            print("Sorry we can not find that username and password combination")

def doLogin2(password='root'):
    if password == 'root':
        print("YES")
    else:
        print("NO, :(")

def createUser(username, password='pasword'):
    user = User(username, password)
    user.process()


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    resetcode = Column(String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.resetcode = ''.join(random.choice(string.ascii_lowercase) for i in range(16))

    def process(self):
        db.session.add(self)
        db.session.commit()
        return self

    def serialize(self):
        return {
            'id': self.id, 
            'username': self.username,
            'password': self.password,
            'resetcode': self.resetcode
        }