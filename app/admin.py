from flask_admin.contrib.pymongo import ModelView
from app import admin, mongo
from app.models import User



# Add views
class UserView(ModelView):
    column_list = ('username', 'email')

admin.add_view(UserView(User, 'Users'))
