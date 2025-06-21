from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:yourpassword@localhost:5432/ai_therapist")

try:
    with engine.connect() as conn:
        print("✅ PostgreSQL connected!")
except Exception as e:
        print("❌ Connection failed:", e)
