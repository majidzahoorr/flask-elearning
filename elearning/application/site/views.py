from flask import Blueprint, render_template
mod = Blueprint('site', __name__, template_folder='templates')
from application.site.forms import ContactForm

@mod.route('/')
@mod.route('/home')
def index():
	return render_template('index.html')	


@mod.route('/contact')
def contact():
	title = 'About Us'
	form = ContactForm()
	return render_template('contact.html', title=title, form=form)

@mod.route('/courses')
def courses():
	title = 'Our Courses'
	return render_template('courses.html', title=title)

@mod.route('/about')
def about():
	title = 'About Us'
	return render_template('about.html', title=title)

@mod.route('/blogs')
def blogs():
	title = 'Blogs'
	return render_template('blogs.html', title=title)			

