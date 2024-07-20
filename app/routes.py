from flask import render_template, jsonify, redirect, url_for, flash
from app import app, mongo
from app import app, admin
# from app.models import User
from app.forms import LoginForm
from app.models import Admin
from pymongo.errors import ServerSelectionTimeoutError

# Function to create or check the database in MongoDB
def create_database():
    try:
        existing_databases = mongo.cx.list_database_names()
        if 'images' not in existing_databases:
            db = mongo.cx['images']  # Access 'images' database
            db.create_collection('image_list')  # Create a collection 'image_list'
            print("Database 'images' created successfully.")
        else:
            print("Database 'images' already exists.")
    except ServerSelectionTimeoutError as e:
        print(f"Error connecting to MongoDB: {e}")

create_database()

# Example route
@app.route('/')
def index():
    db = mongo.db.mydatabase  # Adjust to your database name
    collection = db.mycollection  # Adjust to your collection name
    result = collection.find_one()
    return jsonify(result)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if Admin.check_password(username, password):
            # In a real application, you would set a session variable here
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard
        else:
            flash('Invalid username or password', 'danger')
    return render_template('admin/login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    # Check if admin is logged in (use session or other authentication method)
    return render_template('dashboard.html')