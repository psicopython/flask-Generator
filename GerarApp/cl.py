def config_ex(app):
	app.config["SECRET_KEY"] = ""
	app.config["JWT_SECRET_KEY"] = ""	
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	