from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import hash

@hash.route("/", methods=['GET'])
@register_breadcrumb(hash, '.', 'hash')
def main():
    return render_template("hash/index.html", siteInfo=g, title = "hash", description = "", results="")


@hash.route("/data/", methods=['GET', 'POST'])
def data():
    data = []
    c = Conn_postgres()
    try:
        sql = "SELECT * FROM customers;"
        data = c.exec(sql)
    except:
        pass
    c.close()

    return {'data': data}