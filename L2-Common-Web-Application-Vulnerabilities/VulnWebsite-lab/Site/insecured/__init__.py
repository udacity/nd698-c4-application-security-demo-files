from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

insecured = Blueprint(
    'insecured',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/insecured'
)

from . import views
