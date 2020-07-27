from . import db,ma

#Sua Class começa aqui, exemplo:

#class User(db.Model):
#    __tablename__="User"
#    id = db.Column(db.Integer,primary_key=True)
#    user = db.Column(db.String(64),unique=True,nullable=False)


#class UserSchema(ma.Schema):
#    class Meta:
#        field = ("id","user")

#user_schema = UserSchema()
#userS_schema = UserSchema(many=True)