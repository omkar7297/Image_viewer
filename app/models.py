from app import mongo

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        # Save user data to MongoDB
        mongo.db.users.insert_one({
            'username': self.username,
            'email': self.email
        })

    @staticmethod
    def find_all():
        # Retrieve all users from MongoDB
        return mongo.db.users.find()


class Admin:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @staticmethod
    def check_password(username, password):
        return username == 'admin1', password == 'password1'