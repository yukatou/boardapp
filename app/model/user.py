from app.db.user import UserTable
from app.db import db_session

class UserModel(object):
    @classmethod
    def save(self, username, password):
        user = UserTable(username=username, password=password)
        db_session.add(user)
        db_session.commit()

    @classmethod
    def get(self, username, password):
        user = db_session.query(UserTable).filter(UserTable.username==username).first()
        if user.check_password(password):
            return user
        else:
            return False
