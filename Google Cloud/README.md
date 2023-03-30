# Speech-Translator

This program uses Google Cloud Speech-to-Text and Google Translate APIs to transcribe and translate spoken audio in a variety of languages.

## Requirements

- `python 3.7` or newer
- `speech_recognition` library
- `googletrans` library
- `pyaudio` library
- `google-cloud-speech` library
- Google Cloud credentials

## Installation

1. Clone the repository from Github:

```bash
git clone https://github.com/username/Speech-Translator.git
```

2. Install the necessary libraries:

```bash
pip install -r requirements.txt
```

3. Set up Google Cloud credentials by following the instructions in the [official documentation](https://cloud.google.com/docs/authentication/getting-started).

4. Run the program:

```bash
python speech_translator.py
```

## Usage

1. Speak into the microphone when prompted.

2. The program will transcribe your speech and display the text.

3. The program will then translate the text to English and display the translation.

4. The program will generate two audio files (in Chinese and English) and save them in the folder 'Speaker'.

5. The program will play the audio files in loop until the user terminates the program.

Note: The program only supports Chinese (Traditional) as input language at this moment, but can be easily modified to support other languages by modifying the code.