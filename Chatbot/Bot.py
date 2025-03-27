import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using a list of tuples
pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you?", 
        ["I'm doing well, thank you! How about you?", "I'm great! What about you?"]
    ],
    [
        r"(.*) your name?", 
        ["I'm a chatbot created by John!", "You can call me ChatBot."]
    ],
    [
        r"what can you do?", 
        ["I can chat with you, answer basic questions, and help with simple tasks!"]
    ],
    [
        r"bye|goodbye", 
        ["Goodbye! Have a great day!", "See you later!"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
