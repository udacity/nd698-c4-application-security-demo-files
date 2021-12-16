from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import brokenauth

@brokenauth.route("/", methods=['GET'])
@register_breadcrumb(brokenauth, '.', 'brokenauth')
def main():
    return render_template("brokenauth/index.html", siteInfo=g, title = "brokenauth", description = "", results="")

def cleanvar(data):
    data = data.replace("'","")
    data = data.replace("--","")
    return data

def cleanpwd(data):
    pep = "djf84jgf74j"
    data = data.replace("'","")
    data = data.replace("--","")
    data = pep + data + pep
    return data 

@brokenauth.route("/", methods=['POST'])
def login():
    c = Conn_postgres()
    username = request.values.get('username')
    password = request.values.get('password')

    data = c.exec("SELECT id, role, firstname, lastname, username FROM users2 WHERE role='admin' AND username = '" + cleanvar(username) + "' AND password = md5('" + cleanpwd(password) + "')")
    c.close()

    if(len(data) > 0):
        results = "True"
    else:
        results = "False"

    return render_template("brokenauth/index.html", siteInfo=g, title = "brokenauth", description = "", results=results)

@brokenauth.route("/login2", methods=['POST'])
def login2():
    c = Conn_postgres()
    username = request.values.get('username')
    password = request.values.get('password')

    data = c.exec("SELECT id, role, firstname, lastname, username FROM users2 WHERE role='user' AND username = '" + cleanvar(username) + "' AND password = md5('" + cleanpwd(password) + "')")
    c.close()

    if(len(data) > 0):
        results = "True"
    else:
        results = "False"

    return jsonify(results)
