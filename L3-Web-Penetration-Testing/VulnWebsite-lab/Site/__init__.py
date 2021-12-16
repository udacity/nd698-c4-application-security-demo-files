import os
from flask import Flask
from flask import request, session, redirect, g
from flask_breadcrumbs import Breadcrumbs
from Site.config import Config
from urllib.parse import urlparse

from Site.home import home
from Site.recon import recon
from Site.sqli import sqli
from Site.xss import xss
from Site.brokenauth import brokenauth
from Site.brokenaccess import brokenaccess
from Site.hash import hash

def create_app():
    # Init flask app
    app = Flask(__name__, 
                static_url_path="", 
                static_folder="public"
    )

    # Get Config data
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'dkjdfgasi342098fdakj324hgrf098123i4jklafd09234kj'
    
    # Initialize Flask-Breadcrumbs
    Breadcrumbs(app=app)

    def prepare_flask_request(request):
        url_data = urlparse(request.url)
        return {
            'https': 'on' if request.environ.get('HTTP_X_FORWARDED_PROTO',request.scheme) == 'https' else 'off',
            'http_host': request.host,
            'server_port': request.environ.get('HTTP_X_FORWARDED_PORT', url_data.port),
            'script_name': request.path,
            'get_data': request.args.copy(),
            'post_data': request.form.copy()
        }

    # Create pre-processing for request
    @app.before_request
    def before_request_func():
        g.siteName = app.config['SITENAME']
        g.siteNameShort = app.config['SITENAMESHORT']

    app.register_blueprint(home)
    app.register_blueprint(recon)
    app.register_blueprint(sqli)
    app.register_blueprint(xss)
    app.register_blueprint(brokenauth)
    app.register_blueprint(brokenaccess)
    app.register_blueprint(hash)

    return app

application = create_app()
