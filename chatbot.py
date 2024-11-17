import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt')

# A small set of questions and answers
data = {
    "greeting": ["hello", "hi", "hey", "howdy", "hola"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "how are you": ["how are you", "how's it going", "how do you do"],
    "what is your name": ["what is your name", "what should I call you", "who are you"]
}

# Corresponding responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Howdy!", "Hola!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Bye!"],
    "thanks": ["You're welcome!", "Glad I could help!", "Anytime!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, how about you?", "I'm fine, thanks for asking!"],
    "what is your name": ["I am a chatbot, you can call me Bot.", "I'm Bot, nice to meet you!"]
}

def preprocess(text):
    text = text.lower()
    return ''.join([char for char in text if char not in string.punctuation])

# Example usage
text = "Hello, how are you?"
print(preprocess(text))  # Output: "hello how are you"

def chatbot_response(user_input):
    # Preprocess user input
    user_input = preprocess(user_input)
    
    # List of all possible questions
    questions = sum(data.values(), [])
    
    # Compute the TF-IDF matrix
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(questions + [user_input])
    
    # Compute cosine similarity between user input and predefined questions
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Find the most similar question
    max_sim_index = cosine_similarities.argmax()
    max_sim_question = questions[max_sim_index]
    
    # Identify the category of the question
    for category, questions_list in data.items():
        if max_sim_question in questions_list:
            response = random.choice(responses[category])
            return response
    
    return "Sorry, I didn't understand that."

print("Hello! I am a simple chatbot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)

