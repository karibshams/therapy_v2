from sqlalchemy.orm import Session
from models import JournalEntry, SessionLocal
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.db: Session = SessionLocal()

    def save_entry(self, content):
        entry = JournalEntry(
            content=content,
            timestamp=datetime.utcnow(),
            word_count=len(content.split())
        )
        self.db.add(entry)
        self.db.commit()

    def get_recent_entries(self, limit=10):
        return self.db.query(JournalEntry).order_by(JournalEntry.timestamp.desc()).limit(limit).all()

    def search_entries(self, keyword):
        return self.db.query(JournalEntry).filter(JournalEntry.content.ilike(f"%{keyword}%")).all()

    def get_entry_by_id(self, entry_id):
        return self.db.query(JournalEntry).filter_by(id=entry_id).first()
