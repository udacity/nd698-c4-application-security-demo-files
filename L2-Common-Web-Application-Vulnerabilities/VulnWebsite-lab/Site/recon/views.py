from flask import render_template, make_response
from flask import Flask, redirect
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string

from . import recon

@recon.route("/")
@register_breadcrumb(recon, '.', 'Recon')
def main():
    resp = make_response(render_template("recon/index.html", siteInfo=g, title = "Recon", description = ""))
    resp.set_cookie('userid', '2')
    return resp

@recon.route("/userinfo/", methods=['GET'])
def userinfo():
    c = Conn_postgres()
    
    id = request.cookies.get('userid')
    data = c.exec_safe("SELECT id, role, firstname, lastname, username FROM users WHERE id = %s;", (id,))
    c.close()

    return jsonify(data)

@recon.route("/help", methods=['GET'])
def help():
    data = {
        'info': 'CONGRATS, You found a hidden page'
    }

    return jsonify(data)

@recon.route("projects", methods=['GET'])
@recon.route("user", methods=['GET'])
@recon.route("feed", methods=['GET'])
@recon.route("themes", methods=['GET'])
@recon.route("forums", methods=['GET'])
@recon.route("jobs", methods=['GET'])
@recon.route("business", methods=['GET'])
@recon.route("video", methods=['GET'])
@recon.route("email", methods=['GET'])
@recon.route("books", methods=['GET'])
@recon.route("banner", methods=['GET'])
@recon.route("reviews", methods=['GET'])
@recon.route("view", methods=['GET'])
@recon.route("graphics", methods=['GET'])
@recon.route("/default", methods=['GET'])
@recon.route("/products", methods=['GET'])
@recon.route("/archives", methods=['GET'])
@recon.route("/login", methods=['GET'])
@recon.route("/support", methods=['GET'])
@recon.route("/helper", methods=['GET'])
@recon.route("/articles", methods=['GET'])
@recon.route("/article", methods=['GET'])
@recon.route("/link", methods=['GET'])
@recon.route("/links", methods=['GET'])
def return301():
    return redirect("/", 301)

@recon.route("user", methods=['GET'])
@recon.route("xml", methods=['GET'])
@recon.route("cgi-bin", methods=['GET'])
@recon.route("rss", methods=['GET'])
@recon.route("modules", methods=['GET'])
@recon.route("email", methods=['GET'])
def return401():
    return redirect("/", 401)