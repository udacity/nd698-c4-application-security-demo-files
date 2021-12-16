from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
from . import xss

@xss.route("/", methods=['GET','POST'])
@register_breadcrumb(xss, '.', 'xss')
def main():
    data = {}
    try:
        if request.values.get('username') != None:
            data = {
                'username': request.values.get('username'),
                'password': request.values.get('password')
            }
    except:
        pass

    return render_template("xss/index.html", siteInfo=g, title = "xss", description = "", data= data, rawurl = request.url.replace('%3C','<').replace('%3E','>').replace('%2F','/'))

@xss.route("/getMsg/<int:id>", methods=['GET'])
def getMsg(id):
    c = Conn_postgres()
    data = ""
    try:
        sql = "SELECT chat_id, user_id, body, users.username FROM messages INNER JOIN users ON users.id = messages.user_id WHERE chat_id = %s ORDER BY messages.id ASC;"
        data = c.exec_safe(sql, (id,))
    except:
        pass
    c.close()

    return jsonify(data)

@xss.route("/sendMsg/<int:id>", methods=['POST'])
def sendMsg(id):
    message = request.values.get('msg')

    c = Conn_postgres()
    try:
        c.insert_safe("INSERT INTO messages (chat_id, user_id, body) VALUES (%s,%s,%s);",(id, 2, message))
    except:
        pass
    c.close()

    data = {
        'rawurl': request.url.replace('%3C','<').replace('%3E','>').replace('%2F','/'),
        'postdata':{            
            'message': message
        }
    }

    return jsonify(data)
