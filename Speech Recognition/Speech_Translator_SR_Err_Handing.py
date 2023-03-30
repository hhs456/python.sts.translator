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
    try:
        text = r.recognize_google(audio_data, language='zh-TW')
        print("Text:", text)
        
        # Translate the text into English
        try:
            translation = translator.translate(text, src='zh-tw', dest='en')
            print("Translation:", translation.text)
            
            # Convert the translated text and source text into speech and save the audio files
            try:
                speaker = pyttsx3.init()
                speaker.setProperty('voice', 'zh')
                speaker.say(text)
                speaker.setProperty('voice', 'en')
                speaker.say(translation.text)    
                
                # Save the audio files
                speaker.save_to_file(text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\chinese.mp3')    
                speaker.save_to_file(translation.text, r'D:\User\Documents\GitHub\Speech-Translator\Speaker\english.mp3')
                speaker.runAndWait()
           
            except Exception as e:
                print("Error: Could not convert translated text and source text to speech and save the audio files.", e)
            
        except Exception as e:
            print("Error: Could not translate the text.", e)
        
    except Exception as e:
        print("Error: Could not recognize the audio.", e)  
        
except Exception as e:
    print("Error:", e)