from app.db.user import UserTable
from app.db import db_session

class UserModel(object):
    def get_entries(self):
        return db_session.query(UserTable).all()
    
