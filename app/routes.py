from flask import render_template, jsonify
from app import app, mongo
from app import app, admin
from app.models import User
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
