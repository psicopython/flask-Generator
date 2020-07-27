from flask import Flask

from  app.config import config_app


def create_app():
	app = Flask(__name__)
	config_app(app)
	return app