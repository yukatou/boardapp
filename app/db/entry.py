from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Text
from sqlalchemy.dialects.mysql import INTEGER as Integer

Base = declarative_base()
class EntryTable(Base):
    __tablename__ = 't_entry'
    __table_args__ = {'mysql_engine': 'InnoDB',
                      'mysql_charset': 'utf8'}

    id = Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    title = Column(String(length=255), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(DateTime, default=func.now())

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return "<id:%s title:%s>" % (self.id, self.title)

