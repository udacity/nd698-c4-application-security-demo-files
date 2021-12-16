from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

default_breadcrumb_root(home, '.')

from . import views