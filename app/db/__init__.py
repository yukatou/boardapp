from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from app.settings import DB_CONFIG

db_engine = create_engine(DB_CONFIG)
db_session = scoped_session(sessionmaker(bind=db_engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=db_engine)

def session_remove():
    db_session.remove()
    
