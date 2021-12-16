from flask import render_template, make_response
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import reconexercise

@reconexercise.route("/")
@register_breadcrumb(reconexercise, '.', 'Recon Exercise')
def main():
    return render_template("reconexercise/index.html", siteInfo=g, title = "Recon Exercise", description = "")

@reconexercise.route("/users/", methods=['GET'])
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

@reconexercise.route("/secretpagethatyoudidntknowabout", methods=['GET'])
def secretpage():
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{secretpage542165}'
    }

    return jsonify(data)

@reconexercise.route("/anothersecuritypagethatyoumighthaveneverfoundwithanyscripts", methods=['GET'])
def anothersecuritypage():
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{anothersecuritypage326428}'
    }

    return jsonify(data)

@reconexercise.route("/uploads", methods=['GET'])
def uploads():
    data = {
        'info': 'CONGRATS, You found a hidden page',
        'value': 'flag{uploads154789}'
    }

    return jsonify(data)

@reconexercise.route("projects", methods=['GET'])
@reconexercise.route("user", methods=['GET'])
@reconexercise.route("feed", methods=['GET'])
@reconexercise.route("themes", methods=['GET'])
@reconexercise.route("forums", methods=['GET'])
@reconexercise.route("jobs", methods=['GET'])
@reconexercise.route("business", methods=['GET'])
@reconexercise.route("video", methods=['GET'])
@reconexercise.route("email", methods=['GET'])
@reconexercise.route("books", methods=['GET'])
@reconexercise.route("banner", methods=['GET'])
@reconexercise.route("reviews", methods=['GET'])
@reconexercise.route("view", methods=['GET'])
@reconexercise.route("graphics", methods=['GET'])
@reconexercise.route("/default", methods=['GET'])
@reconexercise.route("/products", methods=['GET'])
@reconexercise.route("/archives", methods=['GET'])
@reconexercise.route("/login", methods=['GET'])
@reconexercise.route("/support", methods=['GET'])
@reconexercise.route("/helper", methods=['GET'])
@reconexercise.route("/articles", methods=['GET'])
@reconexercise.route("/article", methods=['GET'])
@reconexercise.route("/link", methods=['GET'])
@reconexercise.route("/links", methods=['GET'])
def return302():
    return redirect("/", 302)

@reconexercise.route("user", methods=['GET'])
@reconexercise.route("xml", methods=['GET'])
@reconexercise.route("cgi-bin", methods=['GET'])
@reconexercise.route("rss", methods=['GET'])
@reconexercise.route("modules", methods=['GET'])
@reconexercise.route("email", methods=['GET'])
def return401():
    return redirect("/", 401)

