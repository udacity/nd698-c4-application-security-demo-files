from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import sqlisafe

@sqlisafe.route("/")
@register_breadcrumb(sqlisafe, '.', 'sqlisafe')
def main():
    return render_template("sqlisafe/index.html", siteInfo=g, title = "sqlisafe", description = "")

@sqlisafe.route("/login", methods=['POST'])
def login():
    c = Conn_postgres()
    
    sql = ""
    auth = False
    data = []
    
    try:
        username = request.values.get('username')
        password = request.values.get('password')
        sql = "SELECT * FROM users WHERE username = %s AND password = %s;"
        data = c.exec_safe(sql,(username, password))

        if len(data) == 1:
            auth = True
    except:
        pass
    c.close()

    return {'auth': auth, 'sql': sql.replace(username,"<b style='color:red'>" + username + "</b>").replace(password,"<b style='color:red'>" + password + "</b>"), 'data': data}

@sqlisafe.route("/users/<string:id>", methods=['GET'])
def users(id):
    c = Conn_postgres()
    
    sql = ""
    successful = False
    data = []

    id = cleanvalue(id)
    
    try:
        sql = "SELECT * FROM userlist WHERE role = 'user' and id = '" + id + "';"
        data = c.exec(sql)

        for d in data:
            if d[1] == 'admin':
                successful = True
    except:
        pass
    c.close()

    return {'successful': successful, 'sql': sql.replace(id,"<b style='color:red'>" + id + "</b>"), 'data': data}

def cleanvalue(data):
    data = data.replace('-','\\-')
    data = data.replace('\'','\\\'')

    return data