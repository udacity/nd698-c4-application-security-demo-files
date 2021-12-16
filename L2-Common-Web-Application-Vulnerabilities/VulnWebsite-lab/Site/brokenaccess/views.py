from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import brokenaccess

@brokenaccess.route("/", methods=['GET'])
@register_breadcrumb(brokenaccess, '.', 'brokenaccess')
def main():
    return render_template("brokenaccess/index.html", siteInfo=g, title = "brokenaccess", description = "", results="")

@brokenaccess.route("/profile", methods=['GET'])
@register_breadcrumb(brokenaccess, '.', 'brokenaccess')
def profile():
    return render_template("brokenaccess/profile.html", siteInfo=g, title = "brokenaccess", description = "", results="")

@brokenaccess.route("/getuser/<int:userid>", methods=['GET'])
def getuser(userid):
    c = Conn_postgres()
    data = c.exec("SELECT firstname, lastname, role FROM users WHERE id = '" + str(userid) + "'")
    c.close()

    return jsonify(data)

@brokenaccess.route("/secret/", methods=['GET', 'POST'])
def secret():
    data = []
    c = Conn_postgres()
    try:
        sql = "SELECT * FROM secrets;"
        data = c.exec(sql)
    except:
        pass
    c.close()

    return {'data': data}