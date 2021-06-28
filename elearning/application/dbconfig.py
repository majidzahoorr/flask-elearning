from application import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Database Connection
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLAlCHEMY_DATABASE_URI'] = 'postgresql://majid:pakistani@localhost/elearning'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.create_all()

# End Database Connection
