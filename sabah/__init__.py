from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sabah.db'
db = SQLAlchemy(app)



from sabah.admin.routes import admin
from sabah.blog.routes import blog
from sabah.main.routes import main
from sabah.errors.handles import errors

app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(main)
app.register_blueprint(errors)

   


   