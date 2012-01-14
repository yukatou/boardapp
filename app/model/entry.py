from app.db.entry import EntryTable
from app.db import db_session

class EntryModel(object):
    def get_entries(self):
        return db_session.query(EntryTable).all()

    @classmethod
    def save(self, title, text, user_id):
        entry = EntryTable(title, text, user_id)
        db_session.add(entry)
        db_session.commit()

