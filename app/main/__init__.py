from flask import Blueprint

main = Blueprint('main', __name__)

# the modules are imported at the bottom to avoid errors due to circular dependencies
from . import views, errors
