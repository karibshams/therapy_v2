from sqlalchemy.orm import Session
from models import MoodLog, SessionLocal
from datetime import datetime, timedelta

class MoodTracker:
    def __init__(self, user_id):
        self.db: Session = SessionLocal()
        self.user_id = user_id

    def log_mood(self, mood_data):
        entry = MoodLog(
            user_id=self.user_id,
            mood=mood_data["mood"],
            log_time=datetime.utcnow()
        )
        self.db.add(entry)
        self.db.commit()

    def get_mood_history(self, days=30):
        cutoff = datetime.utcnow() - timedelta(days=days)
        return self.db.query(MoodLog).filter(
            MoodLog.user_id == self.user_id,
            MoodLog.log_time > cutoff
        ).all()

    def get_mood_stats(self):
        entries = self.get_mood_history(7)
        if not entries:
            return {}

        return {
            "total_entries": len(entries),
            "recent_entries": len(entries),
            "avg_energy": 0,  
            "avg_anxiety": 0  
        }
