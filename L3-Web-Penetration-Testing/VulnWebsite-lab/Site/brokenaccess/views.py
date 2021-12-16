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