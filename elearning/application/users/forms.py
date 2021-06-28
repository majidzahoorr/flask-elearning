from wtforms import Form, StringField, PasswordField
# from wtforms.validators import InputValidator

class LoginForm(Form):
	username = StringField('Username')
	password = PasswordField('Password')