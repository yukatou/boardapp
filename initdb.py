# coding=utf-8
from app.db.entry import EntryTable
from app.db.user import UserTable
from app.db import db_engine, db_session, init_db

try:
    init_db()
    #UserTable.__table__.create(bind=db_engine)
    #EntryTable.__table__.create(bind=db_engine)
    #db_session.add(ProjectTable('Hello World!'))
    #db_session.add(ProjectTable(u'こんにちは、世界！'))
    #db_session.commit()
except Exception, e:
    print e
    pass
