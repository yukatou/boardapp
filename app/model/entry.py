from app.db.entry import EntryTable
from app.db import db_session

class EntryModel(object):
    def get_entries(self):
        return db_session.query(EntryTable).all()
    
