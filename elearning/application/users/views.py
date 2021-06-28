from flask import Blueprint, render_template
# Defining Blueprint(s)
mod = Blueprint('users', __name__, template_folder='templates')

from application.users.forms import LoginForm


@mod.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
	# error = None
	# if request.method == 'POST':
	# 	if(request.form['username'] != 'admin') \
	# 	or request.form['password'] != 'admin':
	# 		error = 'Invalid Credentials. Please try again.'
	# 	else:
	# 		session['logged_in'] = True
	# 		flash('You were logged in.')
	# 		return redirect(url_for('home'))
	# return render_template('login.html', error=error)			