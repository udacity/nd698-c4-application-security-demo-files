from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
from . import tool
from .hashcracking import HashCracking
from .hashid import HashID

@tool.route("/hashcracking", methods=['GET'])
@register_breadcrumb(tool, '.', 'Tools')
def hashcracking():
    return render_template("tool/hashcracking.html", siteInfo=g, title = "Tools", description = "")

@tool.route("/hashcracking/<string:hash>", methods=['GET'])
def hashcracking_post(hash):
    data = ""
    try:
        c = HashCracking()
        data = c.process(hash)
    except:
        pass

    return jsonify(data)

@tool.route("/hashcrackingtype/<string:hashtype>/<string:hash>", methods=['GET'])
def hashcrackingtype_post(hashtype, hash):
    data = ""
    try:
        c = HashCracking()
        data = c.process(hash)

        if hashtype.lower() == data['algorithm'].replace('PLAIN', '').lower():
            pass
        else:
            data = None
    except:
        pass

    return jsonify(data)

@tool.route("/hashid", methods=['GET'])
@register_breadcrumb(tool, '.', 'Tools')
def hashid():
    return render_template("tool/hashid.html", siteInfo=g, title = "Tools", description = "")

@tool.route("/hashid/<string:hash>", methods=['GET'])
def hashid_post(hash):
    data = ""
    try:
        c = HashID()
        data = c.writeResult(c.identifyHash(hash))
    except:
        pass

    return jsonify(data)