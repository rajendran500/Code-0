import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to user's voice command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""
        except sr.WaitTimeoutError:
            speak("No command detected.")
            return ""

def process_command(command):
    """Processes user commands and responds accordingly."""
    if "hello" in command:
        speak("Hello! How can I help you?")
    
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query} on Wikipedia...")
            try:
                result = wikipedia.summary(query, sentences=1)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("Multiple results found. Can you be more specific?")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results.")
            except wikipedia.exceptions.WikipediaException:
                speak("An error occurred while fetching information from Wikipedia.")
        else:
            speak("Please specify what to search for.")

    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        return False  # Return False to stop the loop
    
    else:
        speak("I'm not sure how to respond to that.")
    
    return True  # Continue the loop

# Main loop
if __name__ == "__main__":
    speak("Hello, I am your AI assistant. How can I assist you today?")
    running = True
    while running:
        user_command = listen()
        if user_command:
            running = process_command(user_command)  # Stop the loop if False is returned


