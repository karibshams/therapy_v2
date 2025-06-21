import os
from typing import List

class Config:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")
    GOOGLE_CLOUD_KEY: str = os.getenv("GOOGLE_CLOUD_KEY", "")
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY", "")

    AI_MODEL: str = "gpt-4o"
    AI_TEMPERATURE: float = 0.6
    MAX_TOKENS: int = 600

    THERAPY_APPROACHES: List[str] = [
        "Cognitive Behavioral Therapy (CBT)",
        "Dialectical Behavior Therapy (DBT)",
        "Acceptance and Commitment Therapy (ACT)",
        "General Supportive"
    ]

    DEFAULT_THERAPY_PROMPT: str = (
        "You are a compassionate mental health therapist specializing in {therapy_style}. "
        "Your goal is to help users cope with anxiety, depression, ADHD, stress, and other mental health challenges. "
        "Use evidence-based techniques and maintain a calm, supportive tone. "
        "If the user is in crisis, recommend contacting a local mental health professional or emergency hotline. "
        "Respond entirely in English. "
        "User says: \"{user_input}\""
    )

    AUTO_DELETE_DAYS: int = 30

    VOICE_LANGUAGES = {
        "English (US)": "en-US"
    }

    VOICE_MODEL: str = "eleven_monolingual_v1"

    DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "postgresql://avnadmin:AVNS_xhTjplH2Cxc_gC-uTeD@pg-qbitcoders-ffindrafiulislam0170-2d82.b.aivencloud.com:17973/karibvai?sslmode=require"
     )
