from flask import render_template, make_response
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
import random
import string
import json

from . import insecured

userinfo = {
    'username': 'jdoe',
    'role': 'user'
}

@insecured.route("/", methods=['GET'])
@register_breadcrumb(insecured, '.', 'insecured')
def main():
    resp = make_response(render_template("insecured/index.html", siteInfo=g, title = "Insecured Deserialization", description = ""))
    resp.set_cookie('auth', json.dumps(userinfo))
    return resp

@insecured.route("/admin-area", methods=['GET'])
@register_breadcrumb(insecured, '.', 'insecured')
def adminarea():
    try:
        auth = request.cookies.get('auth')
        userinfo = json.loads(auth)
        username = userinfo['username']
        role = userinfo['role']
    except:
        username = ""
        role = ""

    if role == 'admin':
        resp = make_response(render_template("insecured/inside.html", siteInfo=g, title = "Insecured Deserialization", description = ""))
    else:
        resp = make_response(render_template("insecured/unauth.html", siteInfo=g, title = "Insecured Deserialization", description = ""))

    return resp

@insecured.route("/pdoe-area", methods=['GET'])
@register_breadcrumb(insecured, '.', 'insecured')
def pdoearea():
    try:
        auth = request.cookies.get('auth')
        userinfo = json.loads(auth)
        username = userinfo['username']
        role = userinfo['role']
    except:
        username = ""
        role = ""

    if username == 'pdoe':
        resp = make_response(render_template("insecured/inside.html", siteInfo=g, title = "Insecured Deserialization", description = ""))
    else:
        resp = make_response(render_template("insecured/unauth.html", siteInfo=g, title = "Insecured Deserialization", description = ""))

    return resp

@insecured.route("/mdoe-accounting-area", methods=['GET'])
@register_breadcrumb(insecured, '.', 'insecured')
def mdoearea():
    try:
        auth = request.cookies.get('auth')
        userinfo = json.loads(auth)
        username = userinfo['username']
        role = userinfo['role']
    except:
        username = ""
        role = ""

    if username == 'mdoe' and role == 'accounting':
        resp = make_response(render_template("insecured/inside.html", siteInfo=g, title = "Insecured Deserialization", description = ""))
    else:
        resp = make_response(render_template("insecured/unauth.html", siteInfo=g, title = "Insecured Deserialization", description = ""))

    return resp