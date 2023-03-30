# Required Libraries
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Google Translate setup
translator = Translator()

# Speech recognition setup
r = sr.Recognizer()
mic = sr.Microphone()

# Define audio recording and transcription function
def record_audio():
    with mic as source:
        print("Please speak now: ")
        audio_data = r.listen(source)
    return audio_data

# Usage
try:
    # Record audio and convert to text
    audio_data = record_audio()
    text = r.recognize_google(audio_data, language='zh-TW')
    print("Text:", text)
    
    # Translate the text into English
    translation = translator.translate(text, src='zh-tw', dest='en')
    print("Translation:", translation.text)
    
    # Convert the translated text and source text into speech and save the audio files
    speaker = pyttsx3.init()
    speaker.setProperty('voice', 'zh')
    speaker.say(text)
    speaker.setProperty('voice', 'en')
    speaker.say(translation.text)    
    
    # Save the audio files
    speaker.save_to_file(text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\chinese.mp3')    
    speaker.save_to_file(translation.text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\english.mp3')
    speaker.runAndWait()    
    
except Exception as e:    print("Error:", e)
