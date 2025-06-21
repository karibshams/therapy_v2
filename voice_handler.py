import os
import openai
from elevenlabs.client import ElevenLabs
from elevenlabs import play, VoiceSettings
from dotenv import load_dotenv

load_dotenv()

# Set API keys
openai.api_key = os.getenv("OPENAI_API_KEY")

class VoiceHandler:
    def __init__(self):
        self.tts_enabled = True
        self.stt_enabled = True
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    def speech_to_text(self, audio_file):
        """Convert speech to text using OpenAI Whisper API"""
        try:
            with open(audio_file, "rb") as audio:
                transcript = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio,
                    response_format="text"
                )
            return transcript
        except Exception as e:
            return f"Error in speech-to-text: {str(e)}"

    def text_to_speech(self, text):
        """Convert text to speech using ElevenLabs"""
        try:
            audio = self.client.generate(
                text=text,
                voice="Rachel",
                model="eleven_monolingual_v1",
                voice_settings=VoiceSettings(stability=0.4, similarity_boost=0.75)
            )
            play(audio)
        except Exception as e:
            return f"Error in text-to-speech: {str(e)}"

    def detect_emotion_from_text(self, text):
        """Use GPT to estimate emotional tone from text"""
        try:
            prompt = f"What is the emotional tone of this message?\nMessage: \"{text}\""
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message["content"]
        except Exception as e:
            return "neutral"
