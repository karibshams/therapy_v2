
# 🧠 MindCare AI Therapy

**MindCare AI Therapy** is a Streamlit-based intelligent mental health assistant. It offers an AI-powered therapist chat, mood tracking, journaling, PDF workbook support, and session history—all integrated into a privacy-conscious mental wellness platform.

---

## 🚀 Features

- 🤖 **AI Therapist Chat**: Chat with a GPT-4o-powered virtual therapist using evidence-based mental health approaches like CBT, DBT, and ACT.
- 📊 **Mood Tracker**: Log and visualize your mood trends.
- 📔 **Journal**: Maintain a daily mental health journal.
- 📚 **Therapy Workbook**: Upload and view guided PDF therapy workbooks.
- 🕑 **Session History**: Review past therapy conversations.
- 🔊 **Voice Support**: Input via speech-to-text and receive responses via text-to-speech using ElevenLabs.
- 🌐 **Multilingual Support** (extensible).
- 🛡️ **Data Privacy**: Sessions are stored in PostgreSQL and auto-deleted after 30 days.

---

## 🧩 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: `gpt-4o` (via OpenAI API)
- **Voice API**: ElevenLabs (Text-to-Speech), Google Cloud (Speech-to-Text)
- **Database**: PostgreSQL (Aiven Cloud)
- **Libraries**: `pandas`, `fitz` (PyMuPDF), `apscheduler`, `streamlit`, `psycopg2`, `sqlalchemy`

---

## 📁 Folder Structure

```

Mental\_health\_AI\_Therapy/
│
├── ai\_therapist.py           # GPT-4o therapist logic
├── app.py                    # Streamlit frontend
├── config.py                 # Configuration (keys, model, prompts)
├── voice\_handler.py          # Text-to-speech and speech-to-text
├── mood\_tracker.py           # Mood logging and visualization
├── journal\_manager.py        # Journal entry handling
├── session\_manager.py        # Session and history storage
├── rag\_chat.py / rag\_loader.py  # (Optional) RAG integration
├── create\_db.py              # Initialize PostgreSQL schema
├── requirements.txt
├── README.md
├── .env                      # Environment variables (not tracked)
├── vectorstore/              # (For embeddings)
├── pdfs/                     # PDF workbook uploads
└── venv/                     # Virtual environment (excluded from Git)

````

---

## 🛠️ Setup Instructions

1. **Clone the Repo**  
   ```bash
   git clone https://github.com/karibshams/therapy_v2.git
   cd therapy_v2
````

2. **Create a `.env` File**
   Add the following:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ELEVENLABS_API_KEY=your-elevenlabs-api-key
   GOOGLE_CLOUD_KEY=your-google-json-key
   ENCRYPTION_KEY=your-encryption-key
   DATABASE_URL=your-postgresql-url
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**

   ```bash
   python create_db.py
   ```

5. **Run the App**

   ```bash
   streamlit run app.py
   ```

---

## 📌 Notes

* Set up PostgreSQL using Aiven or any cloud provider.
* ElevenLabs API is needed for realistic text-to-speech.
* Google Cloud credentials required for STT.
* Sessions are auto-deleted every 30 days using `apscheduler`.

---

## 📜 License

MIT License © 2025 [Karib Shams](https://github.com/karibshams)

---

## 💬 Contact

Feel free to reach out:

* 📧 Email: [shams321karib@gmail.com](mailto:shams321karib@gmail.com)
* 🌐 LinkedIn: [karib-shams](https://www.linkedin.com/in/karib-shams-007975305)
* 🔗 GitHub: [karibshams](https://github.com/karibshams)

