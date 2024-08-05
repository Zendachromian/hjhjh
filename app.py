from flask import Flask, render_template
from config import Config
from database import db
from models import *


def startapp():
    app = Flask(__name__)  
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # if admin exists, else create admin
        # admin = User.query.filter_by(is_admin=True).first()
        # if not admin:
        #     password_hash = generate_password_hash('admin')
        #     admin = User(username='admin', passhash=password_hash, name='Admin', is_admin=True)
        #     db.session.add(admin)
        #     db.session.commit()
    return app

app = startapp()
from routes import *


if __name__ == '__main__':
    app.run(debug=True)


