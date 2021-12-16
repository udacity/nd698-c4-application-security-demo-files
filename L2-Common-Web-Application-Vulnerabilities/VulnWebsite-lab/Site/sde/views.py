from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
from . import sde

@sde.route("/", methods=['GET','POST'])
@register_breadcrumb(sde, '.', 'sde')
def main():
    
    return render_template("sde/index.html", siteInfo=g, title = "Sensitive Data Exposure", description = "")

@sde.route("/friendlist/", methods=['GET'])
def friendlist():
    c = Conn_postgres()
    
    sql = ""
    data = []
    
    try:
        sql = "SELECT * FROM friendlist;"
        data = c.exec(sql)
    except:
        pass
    c.close()

    return {'data': data}

@sde.route("/customers/", methods=['GET'])
def customers():
    c = Conn_postgres()
    
    sql = ""
    data = []
    
    try:
        sql = "SELECT * FROM customers;"
        data = c.exec(sql)
    except:
        pass
    c.close()

    return {'data': data}