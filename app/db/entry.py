from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Text
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.db.user import UserTable
from app.db import Base

class EntryTable(Base):
    __tablename__ = 't_entry'
    __table_args__ = {'mysql_engine': 'InnoDB',
                      'mysql_charset': 'utf8'}

    id = Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    title = Column(String(length=255), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('t_user.id'), nullable=False)
    user = relationship("UserTable", backref='entry', lazy='join')

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return "<id:%s title:%s>" % (self.id, self.title)

