# coding: utf-8
import speech_recognition as sr
from googletrans import Translator
import pyaudio
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
import os
import pyttsx3

# Google Translate setup
translator = Translator()

# Speech recognition setup
r = sr.Recognizer()
mic = sr.Microphone()


# Set up Google Cloud credentials
key_path = r"D:\User\Documents\GitHub\Speech-Translator\Google API\speech-translator.json"
creds = service_account.Credentials.from_service_account_file(key_path)
client = speech.SpeechClient(credentials=creds)


# Define audio recording and transcription functions
def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                        frames_per_buffer=1024)

    print('Recording...')
    frames = []
    for i in range(0, int(16000 / 1024 * 5)):
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return b''.join(frames)


def transcribe_audio(audio_data, lang='zh-TW'):
    audio_source = speech.types.RecognitionAudio(content=audio_data)
    config = speech.types.RecognitionConfig(language_code=lang)
    response = client.recognize(config, audio_source)
    text = response.results[0].alternatives[0].transcript
    return text


# Define function to play audio
def play_audio(audio_path):
    os.system("afplay " + audio_path)


# Usage
with mic as source:
    print("Please speak now: ")
    audio_data = r.listen(source)

try:
    text = r.recognize_google(audio_data, language='zh-TW')
    print("Text:", text)
    translation = translator.translate(text, src='zh-tw', dest='en')
    print("Translation:", translation.text)
    
    # Convert translated text to speech and save to file
    speaker = pyttsx3.init()
    speaker.setProperty('voice', 'zh')
    speaker.say(text)
    speaker.setProperty('voice', 'en')
    speaker.say(translation.text)    
    
    # Save the audio file
    speaker.save_to_file(text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\chinese.mp3')    
    speaker.save_to_file(translation.text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\english.mp3')
    
    # Run
    speaker.runAndWait()        
    
except Exception as e:
    print("Error:", e)

audio_data = record_audio()
text = transcribe_audio(audio_data, lang='zh-TW')
print('Transcript:', text)
