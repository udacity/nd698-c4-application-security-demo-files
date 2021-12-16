from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

xss = Blueprint(
    'xss',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/xss'
)

from . import views