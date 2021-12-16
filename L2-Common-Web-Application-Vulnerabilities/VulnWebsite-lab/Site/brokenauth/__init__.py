from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

brokenauth = Blueprint(
    'brokenauth',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/brokenauth'
)

from . import views
