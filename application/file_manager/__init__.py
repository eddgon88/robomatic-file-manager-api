# application/order_api/__init__.py
from flask import Blueprint

file_manager_blueprint = Blueprint('file_manager', __name__)

from . import routes