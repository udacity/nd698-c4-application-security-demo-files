from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

brokenaccess = Blueprint(
    'brokenaccess',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/brokenaccess'
)

from . import views
