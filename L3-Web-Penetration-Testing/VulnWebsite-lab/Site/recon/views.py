from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import recon

@recon.route("/")
@register_breadcrumb(recon, '.', 'recon')
def main():
    return render_template("recon/index.html", siteInfo=g, title = "recon", description = "")

@recon.route("/users/", methods=['GET'])
def users():
    c = Conn_postgres()
    
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{userspage546254}',
        'data': []
    }

    data['data'] = c.exec("SELECT id, role, firstname, lastname, username FROM users WHERE role = 'user';")
    c.close()

    return jsonify(data)

@recon.route("/secretpagethatyoudidntknowabout", methods=['GET'])
def secretpage():
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{secretpage542165}'
    }

    return jsonify(data)

@recon.route("/anothersecuritypagethatyoumighthaveneverfoundwithanyscripts", methods=['GET'])
def anothersecuritypage():
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{anothersecuritypage326428}'
    }

    return jsonify(data)

@recon.route("/uploads", methods=['GET'])
def uploads():
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{uploads154789}'
    }

    return jsonify(data)