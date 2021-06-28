from flask import Flask 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'majid@zahoor@SECRET_KEY123'

####################### Assets Bundling ######################
##############################################################

from application.users.views import mod
from application.site.views import mod

app.register_blueprint(users.views.mod)
app.register_blueprint(site.views.mod)