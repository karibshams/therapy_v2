from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from config import Config  

Base = declarative_base()
engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)                # ✅ NEW
    age = Column(Integer)               # ✅ NEW
    issue = Column(String)              # ✅ NEW
    created_at = Column(DateTime, default=datetime.utcnow)
    sessions = relationship("SessionModel", back_populates="user")

class SessionModel(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String)
    response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="sessions")

class MoodLog(Base):
    __tablename__ = "moods"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    mood = Column(String)
    energy = Column(Integer)
    anxiety = Column(Integer)
    triggers = Column(String)
    notes = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class JournalEntry(Base):
    __tablename__ = "journals"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(String)
    word_count = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

def create_tables():
    Base.metadata.create_all(bind=engine)