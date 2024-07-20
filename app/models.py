from app import mongo

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        mongo.db.users.insert_one({
            'omkar': self.username,
            'omkar@gmail.com': self.email
        })

    @staticmethod
    def find_all():
        return mongo.db.users.find()