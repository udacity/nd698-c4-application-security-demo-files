from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

hash = Blueprint(
    'hash',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/hash'
)

from . import views
