from flask import Blueprint
from flask_breadcrumbs import default_breadcrumb_root

recon = Blueprint(
    'recon',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/recon'
)

from . import views