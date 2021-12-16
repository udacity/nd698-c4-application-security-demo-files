from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

sde = Blueprint(
    'sde',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/sde'
)

from . import views