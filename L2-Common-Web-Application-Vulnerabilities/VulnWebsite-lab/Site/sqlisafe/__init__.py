from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

sqlisafe = Blueprint(
    'sqlisafe',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/sqlisafe'
)

from . import views