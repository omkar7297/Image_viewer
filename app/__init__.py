from flask import Flask
from flask_admin import Admin
from flask_pymongo import PyMongo

app = Flask(__name__)

# MySQL configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'username'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'Database'

# MongoDB configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app) 

# Create admin
admin = Admin(app, name='Flask-MongoDB Admin', template_mode='bootstrap3')

from app import routes, models