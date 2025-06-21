import streamlit as st
import pandas as pd
from datetime import datetime
from ai_therapist import AITherapist
from voice_handler import VoiceHandler
from mood_tracker import MoodTracker
from journal_manager import JournalManager
from session_manager import SessionManager
from config import Config
import tempfile
from apscheduler.schedulers.background import BackgroundScheduler  

st.set_page_config(
    page_title="MindCare AI Therapy",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'session_manager' not in st.session_state:
    st.session_state.session_manager = SessionManager()
if 'ai_therapist' not in st.session_state:
    st.session_state.ai_therapist = AITherapist()
if 'voice_handler' not in st.session_state:
    st.session_state.voice_handler = VoiceHandler()
if 'mood_tracker' not in st.session_state:
    st.session_state.mood_tracker = MoodTracker(st.session_state.session_manager.user_id)
if 'journal_manager' not in st.session_state:
    st.session_state.journal_manager = JournalManager()
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = list(Config.VOICE_LANGUAGES.values())[0]

if 'scheduler' not in st.session_state:
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        st.session_state.session_manager.auto_delete_old_sessions,
        trigger='interval',
        days=1
    )
    scheduler.start()
    st.session_state.scheduler = scheduler

def main():
    st.title("🧠 MindCare AI Therapy Platform")
    st.markdown("*Your personal AI-powered mental health companion*")

    with st.sidebar:
        st.header("Navigation")
        page = st.selectbox(
            "Choose a feature:",
            ["AI Therapist Chat", "Mood Tracker", "Journal", "Session History", "Workbook", "Settings"]
        )

        st.markdown("---")
        st.subheader("Language: English (US)")  

        st.markdown("---")
        st.subheader("Quick Stats")
        sessions_count = len(st.session_state.session_manager.get_sessions())
        st.metric("Total Sessions", sessions_count)

        if sessions_count > 0:
            last_session = st.session_state.session_manager.get_latest_session()
            st.metric("Last Session", last_session.timestamp.strftime("%Y-%m-%d"))

    if page == "AI Therapist Chat":
        ai_therapist_page()
    elif page == "Mood Tracker":
        mood_tracker_page()
    elif page == "Journal":
        journal_page()
    elif page == "Session History":
        session_history_page()
    elif page == "Workbook":
        workbook_page()
    elif page == "Settings":
        settings_page()

def ai_therapist_page():
    st.header("🧠 AI Therapist Chat")

    col1, col2 = st.columns([3, 1])
    with col1:
        input_mode = st.radio("Input Mode:", ["Text", "Voice"], horizontal=True)
    with col2:
        if st.button("Clear Chat"):
            st.session_state.session_manager.clear_current_session()
            st.rerun()

    chat_container = st.container()
    with chat_container:
        st.subheader("Conversation")
        current_session = st.session_state.session_manager.get_current_session()

        st.text_area("Transcript:", current_session.message + "\n" + current_session.response, height=300)

    st.markdown("---")

    if input_mode == "Text":
        user_input = st.chat_input("Type your message here...")
        if user_input:
            process_user_input(user_input)
    else:
        audio_file = st.file_uploader("🎤 Upload your voice (MP3/WAV):", type=["mp3", "wav"])
        if audio_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_file.read())
                tmp_path = tmp.name
            text = st.session_state.voice_handler.speech_to_text(tmp_path)
            process_user_input(text, is_voice=True)

def process_user_input(user_input, is_voice=False):
    st.session_state.session_manager.add_message("user", user_input)

    ai_response = st.session_state.ai_therapist.get_response(
        user_input,
        language=st.session_state.selected_language
    )

    st.session_state.session_manager.add_message("assistant", ai_response)

    if is_voice:
        st.session_state.voice_handler.text_to_speech(ai_response)

    st.rerun()

def workbook_page():
    import fitz  # PyMuPDF
    st.header("📚 Therapy Workbook")

    uploaded_file = st.file_uploader("Upload a PDF Workbook", type=["pdf"])
    if uploaded_file:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page_num in range(len(doc)):
            st.image(doc.load_page(page_num).get_pixmap().tobytes("png"))

def mood_tracker_page():
    st.header("📊 Mood Tracker")
    # [.. same as previous logic, just ensure PostgreSQL usage ..]

def journal_page():
    st.header("📔 Journal")
    # [.. same as previous logic, now saves to PostgreSQL ..]

def session_history_page():
    st.header("📋 Session History")
    sessions = st.session_state.session_manager.get_sessions()
    for s in sessions:
        with st.expander(f"Session {s.id} - {s.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"):
            st.text(s.message)
            st.text(s.response)

def settings_page():
    st.header("⚙️ Settings")
    st.write("Settings are mostly fixed in this prototype. More to come.")

if __name__ == "__main__":
    main()
