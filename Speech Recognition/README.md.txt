## Speech Translator

This is a Python script that transcribes and translates speech from Chinese (Traditional) to English. It uses the following libraries:

- `speech_recognition` for speech recognition
- `googletrans` for translation
- `pyaudio` for audio recording and playback
- `os` for file management
- `pyttsx3` for text to speech conversion

### Usage

1. Install the required libraries by running `pip install -r requirements.txt` in your terminal.
2. Run the script.
3. When prompted, speak in Chinese (Traditional).
4. The script will transcribe and translate your speech to English.
5. It will also convert the translated text to speech and save the audio files to the `Speaker` directory.

### Note

This script has only been tested on macOS. If you're using a different operating system, you may need to modify the `play_audio()` function in order to play the audio files.