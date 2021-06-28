# from application import db

# class Users(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username):
#     	self.username = username

#     def __repr__(self):
#         return "{}".format(self.username)