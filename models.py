from flask import Flask, request, redirect, abort, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

migrate = Migrate(app, db)



from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

if __name__ == "__main__":
    # print(app.url_for('user', name='John'))
    # db.drop_all()
    # db.create_all()
    # admin_role = Role(name='Admin')
    # mod_role = Role(name='Moderator')
    # user_role = Role(name='User')
    # user_john = User(username='john', role=admin_role)
    # user_susan = User(username='susan', role=user_role)
    # user_david = User(username='david', role=user_role)
    # db.session.add_all([admin_role, mod_role, user_role,
    #                     user_john, user_susan, user_david])
    #
    # db.session.commit()

    # print(admin_role.id)
    # print(mod_role.id)
    # print(admin_role.name)
    # admin_role.name = 'Administrator'
    # db.session.add(admin_role)
    # db.session.commit()

    # print(User.query.filter_by(role=user_role).all())
    # send_email()
    # app.run()

    u = User()

    u.password = 'cattle'
    print(u.password_hash)
    print(u.verify_password('cattle'))
