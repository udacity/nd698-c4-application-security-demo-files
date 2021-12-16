from flask import render_template
from flask import session, g
from flask import request, jsonify
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from Site.db import Conn_postgres
from flask import current_app as app
from . import xss

@xss.route("/")
@register_breadcrumb(xss, '.', 'xss')
def main():
    c = Conn_postgres()
    data = c.exec("SELECT chat_id, user_id, body, users.username FROM messages INNER JOIN users ON users.id = messages.user_id WHERE chat_id = '2' ORDER BY messages.id ASC;")
    c.close()

    return render_template("xss/index.html", siteInfo=g, title = "xss", description = "", chat_msg = data)

def cleanvar(data):
    data = data.replace("'","")
    data = data.replace("--","")
    return data

def cleanvar2(data):
    data = cleanvar(data)
    if "script" in data.lower():
        data = data.lower().replace("script","")
    
    return data

@xss.route("/getMsg/<int:id>", methods=['GET'])
def getMsg(id):
    c = Conn_postgres()
    try:
        data = c.exec("SELECT chat_id, user_id, body, users.username FROM messages INNER JOIN users ON users.id = messages.user_id WHERE chat_id = '" + str(id) + "' ORDER BY messages.id ASC;")
    except:
        pass
    c.close()

    return jsonify(data)

@xss.route("/sendMsg/<int:id>", methods=['POST'])
def sendMsg(id):
    user_id = 2
    message = request.values.get('msg')

    c = Conn_postgres()
    try:
        c.insert("INSERT INTO messages (chat_id, user_id, body) VALUES (" + str(id) + "," + str(user_id) +",'" + cleanvar(message) + "');")
    except:
        pass
    c.close()

    return jsonify("Done")

@xss.route("/sendMsg2/<int:id>", methods=['POST'])
def sendMsg2(id):
    user_id = 2
    message = request.values.get('msg')

    c = Conn_postgres()
    try:
        c.insert("INSERT INTO messages (chat_id, user_id, body) VALUES (" + str(id) + "," + str(user_id) +",'" + cleanvar2(message) + "');")
    except:
        pass
    c.close()

    return jsonify("Done")