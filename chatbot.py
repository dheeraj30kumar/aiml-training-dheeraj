import nltk
import random
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey, how can I help you?']),
    (r'how are you?', ['I am doing well, thank you!', 'I am great, how about you?']),
    (r'what is your name?', ['I am a chatbot. You can call me Chatbot!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'It was nice talking to you!']),
    (r'how can you help me?', ['I can chat with you, answer questions, and assist you with basic tasks.']),
    (r'(.*) your name?', ['My name is Chatbot!']),
    (r'(.*) (help|assist|support)', ['Sure! How can I assist you today?']),
    (r'(.*)', ['Sorry, I didn’t understand that. Could you rephrase?'])
]

# Create the chatbot using the patterns and reflections
chatbot = Chat(patterns, reflections)

# Start chatting with the bot
def start_chat():
    print("Hello! I am Chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in 
