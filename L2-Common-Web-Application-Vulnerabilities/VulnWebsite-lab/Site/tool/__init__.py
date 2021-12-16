from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

tool = Blueprint(
    'tool',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/tool'
)

from . import views