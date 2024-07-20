import os
from flask import Flask
from flask_admin import Admin
from flask_pymongo import PyMongo
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder='templates/')

# MySQL configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'username'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'Database'

# MongoDB configuration     
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
csrf = CSRFProtect(app)
mongo = PyMongo(app) 

# Create admin
admin = Admin(app, name='Flask-MongoDB Admin', template_mode='bootstrap3')  
from app import routes, models