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
    
    # Save recognized text to a file
    with open('recognized_text.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        print("Recognized text saved to file.")
    
    # Translate the text into English
    translation = translator.translate(text, src='zh-tw', dest='en')
    translated_text = translation.text
    print("Translation:", translated_text)
    
    # Save translated text to a file
    with open('translated_text.txt', 'w', encoding='utf-8') as f:
        f.write(translated_text)
        print("Translated text saved to file.")
    
    # Convert the translated text and source text into speech and save the audio files
    speaker = pyttsx3.init()
    speaker.setProperty('voice', 'zh')
    speaker.say(text)
    speaker.setProperty('voice', 'en')
    speaker.say(translated_text)    
    
    # Save the audio files
    speaker.save_to_file(text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\chinese.mp3')    
    speaker.save_to_file(translated_text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\english.mp3')
    speaker.runAndWait()    
    
except Exception as e:    
    print("Error:", e)
