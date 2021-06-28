from wtforms import Form, StringField, PasswordField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class ContactForm(Form):
	name = StringField('Your Name', render_kw={"placeholder": "Your Name"}, validators=[DataRequired()])
	email = StringField('Your Email', render_kw={"placeholder": "Your E-mail"}, validators=[DataRequired()])
	subject = StringField('Subject', render_kw={"placeholder": "Subject"}, validators=[DataRequired()])
	message = StringField('Message', widget=TextArea(), render_kw={"placeholder": "Message"})