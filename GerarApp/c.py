from .config   import config_ex
from app.model import config_db
from app.views import config_vw


def config_app(app):
	config_ex(app)
	config_db(app)
	config_vw(app)