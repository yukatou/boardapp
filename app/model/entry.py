from app.db.entry import EntryTable
from app.db import db_session
from sqlalchemy.sql.expression import desc

class EntryModel(object):
  @classmethod
  def get_all_count(self):
    return db_session.query(EntryTable).count()

  @classmethod
  def get_entries(self, start, end):
    return db_session.query(EntryTable).order_by(desc(EntryTable.created_date)).all()[start:end]

  @classmethod
  def save(self, title, text, username):
    entry = EntryTable(title, text, username)
    db_session.add(entry)
    db_session.commit()

