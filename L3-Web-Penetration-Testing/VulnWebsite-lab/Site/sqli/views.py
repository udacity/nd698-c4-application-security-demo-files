from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import sqli

@sqli.route("/")
@register_breadcrumb(sqli, '.', 'sqli')
def main():
    return render_template("sqli/index.html", siteInfo=g, title = "sqli", description = "")

@sqli.route("/users/<string:id>", methods=['GET', 'POST'])
def users(id):
    data = []
    c = Conn_postgres()
    try:
        sql = "SELECT id, role, firstname, lastname, username FROM users WHERE role = 'user' and id = '" + id + "' and role = 'user';"
        data = c.exec(sql)
    except:
        pass
    c.close()

    return {'sql': sql, 'data': data}

@sqli.route("/login", methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
    else:
        username = request.args.get('username')
        password = request.args.get('password')

    data = []
    c = Conn_postgres()
    try:
        sql = "SELECT id, role, firstname, lastname, username FROM users WHERE username = '" + username.replace("'","") + "' AND password = MD5('" + password + "');"
        data = c.exec(sql)
    except:
        pass
    c.close()

    return {'sql': sql, 'data': data}

