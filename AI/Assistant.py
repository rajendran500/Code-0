from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import random
import datetime
import threading
import webbrowser

# Speak in English
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = ""
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Listen to voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't understand.")
        return ""

# Web search
def search_web(query):
    speak(f"Searching the web for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Process commands
def process_command(command):
    if "play music" in command:
        music_folder = "C:\\Users\\Admin\\Music\\MEmu Music"
        songs = [file for file in os.listdir(music_folder) if file.endswith((".mp3", ".wav"))]
        if songs:
            song_to_play = random.choice(songs)
            os.startfile(os.path.join(music_folder, song_to_play))
            speak(f"Playing {song_to_play}")
        else:
            speak("No music files found.")

    elif "search" in command or "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        if query:
            search_web(query)
        else:
            speak("Please tell me what to search for.")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        os._exit(0)

    else:
        speak("Sorry, I don't know that command yet.")

# Welcome message
def welcome_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! I'm ready.")
    elif hour < 18:
        speak("Good afternoon! I'm here.")
    else:
        speak("Good evening! I'm listening.")

# Background listener with wake word
def background_listener():
    while True:
        command = listen()
        if "hello assistant" in command or "hey assistant" in command:
            speak("Yes, how can I help you?")
            command = listen()
            process_command(command)

# Run the assistant
def run_ai():
    welcome_user()
    listener_thread = threading.Thread(target=background_listener)
    listener_thread.daemon = True
    listener_thread.start()

    # Keep script alive
    while True:
        pass

run_ai()
