from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Sabah.db'
app.config['SECRET_KEY'] = 'ba2c7f4bb038e6c2b9eae4f3e809013b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)






from sabah.admin.routes import admin
from sabah.blog.routes import blog
from sabah.main.routes import main
from sabah.errors.handles import errors

app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(main)
app.register_blueprint(errors)

   


   