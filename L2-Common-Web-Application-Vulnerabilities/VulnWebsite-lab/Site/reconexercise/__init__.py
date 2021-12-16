from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

reconexercise = Blueprint(
    'reconexercise',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/reconexercise'
)

from . import views