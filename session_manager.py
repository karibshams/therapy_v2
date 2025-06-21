from sqlalchemy.orm import Session
from models import SessionModel, User, SessionLocal
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self):
        self.db: Session = SessionLocal()
        self.user_id = self._get_or_create_user()
        self.current_session_id = self._create_new_session()

    def _get_or_create_user(self):
        user = self.db.query(User).first()
        if not user:
            user = User(name="Anonymous", age=0, issue="General")
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        return user.id

    def _create_new_session(self):
        new_session = SessionModel(user_id=self.user_id, message="", response="")
        self.db.add(new_session)
        self.db.commit()
        self.db.refresh(new_session)
        return new_session.id

    def get_current_session(self):
        return self.db.query(SessionModel).filter_by(id=self.current_session_id).first()

    def add_message(self, role, content, emotion=None):
        session = self.get_current_session()
        if role == "user":
            session.message += f"[{datetime.now()}] User: {content}\n"
        else:
            session.response += f"[{datetime.now()}] AI: {content}\n"
        self.db.commit()

    def get_sessions(self):
        return self.db.query(SessionModel).all()

    def get_latest_session(self):
        return self.db.query(SessionModel).order_by(SessionModel.timestamp.desc()).first()

    def clear_current_session(self):
        session = self.get_current_session()
        session.message = ""
        session.response = ""
        self.db.commit()

    def auto_delete_old_sessions(self, days=30):
        cutoff = datetime.utcnow() - timedelta(days=days)
        old_sessions = self.db.query(SessionModel).filter(SessionModel.timestamp < cutoff).all()
        count = len(old_sessions)
        for s in old_sessions:
            self.db.delete(s)
        self.db.commit()
        return count
