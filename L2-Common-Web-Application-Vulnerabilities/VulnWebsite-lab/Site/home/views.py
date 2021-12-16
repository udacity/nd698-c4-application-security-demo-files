from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from . import home
from flask import current_app as app

@home.route("/")
@register_breadcrumb(home, '.', 'Home')
def main():
    return render_template("index.html", siteInfo=g, title = "Home", description = "")

@home.route("/reset")
def reset():
    c = Conn_postgres()
    try:
        c.setup()
        results = "Done"
    except Exception as err:
        print(err)
        results = "Error"
    c.close()

    return jsonify(message=results)