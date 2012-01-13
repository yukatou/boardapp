from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime
from sqlalchemy.dialects.mysql import INTEGER as Integer
from werkzeug import generate_password_hash, check_password_hash

Base = declarative_base()
class UserTable(Base):
    __tablename__ = 't_user'
    __table_args__ = {'mysql_engine': 'InnoDB',
                      'mysql_charset': 'utf8'}

    id = Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    username = Column(String(length=32), nullable=False, unique=True)
    password = Column(String(length=80), nullable=False)
    created_date = Column(DateTime, default=func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "<id:%s username:%s>" % (self.id, self.username)

    def check_password(self, password):
        return check_password_hash(self.password, password)

