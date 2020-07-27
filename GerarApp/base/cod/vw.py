from flask import Blueprint
from .views import *


bp = Blueprint("webiu",__name__)

bp.add_url_rule("/",methods=["GET"],
	view_func=index,endpoint="index")
	
#bp.add_url_rule("",methods=[],
#	view_func=,endpoint="")

#bp.add_url_rule("",methods=[],
#	view_func=,endpoint="")

#bp.add_url_rule("",methods=[],
#	view_func=,endpoint="")

#bp.add_url_rule("",methods=[],
#	view_func=,endpoint="")

#bp.add_url_rule("",methods=[],
#	view_func=,endpoint="")

#bp.add_url_rule("",methods=[],
#	view_func=,endpoint="")


def config_vw(app):
	app.register_blueprint(bp)