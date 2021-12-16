from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

sqli = Blueprint(
    'sqli',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/sqli'
)

from . import views