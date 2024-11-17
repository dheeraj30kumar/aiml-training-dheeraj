# Simple Chatbot Using Machine Learning

This is a basic chatbot built using machine learning techniques. The chatbot uses Natural Language Processing (NLP) to understand and respond to user queries. It employs TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction and Cosine Similarity for comparing the user's input with predefined questions.

## Features

- Basic text-based interaction.
- Responds to simple queries such as greetings, farewells, and basic questions.
- Uses cosine similarity to find the most relevant response based on predefined questions.

## Requirements

- Python 3.x
- Required libraries:
  - `nltk`
  - `numpy`
  - `pandas`
  - `scikit-learn`

You can install the required libraries using the following command:

```bash
pip install numpy pandas scikit-learn nltk
```

## Setup Instructions

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/your-username/simple-chatbot.git
   cd simple-chatbot
   ```

2. **Download the `punkt` tokenizer from NLTK** (if you haven't done this yet):
   Open a Python shell and run:
   ```python
   import nltk
   nltk.download('punkt')
   ```

3. **Run the Chatbot**:
   After setting up the environment, you can run the chatbot using the following command:
   ```bash
   python chatbot.py
   ```

   The chatbot will start and prompt you for input. Type your queries and the chatbot will respond. Type `exit` to stop the conversation.

## How It Works

### 1. **Data Setup**
   The chatbot is pre-configured with a set of sample questions and corresponding responses. The main categories are:
   - **Greeting**: Responds to user greetings such as "Hello", "Hi", etc.
   - **Goodbye**: Responds to user farewells such as "Goodbye", "Bye", etc.
   - **Thanks**: Responds to "thank you" messages.
   - **How are you**: Responds to queries asking about the bot's well-being.
   - **Name**: Responds to queries asking for the bot's name.

### 2. **Preprocessing**
   - The user input is converted to lowercase.
   - Punctuation is removed for cleaner tokenization.

### 3. **TF-IDF Vectorization**
   - The chatbot converts all questions and user input into numerical vectors using the **TF-IDF** method, which measures the importance of each word in the context of the dataset.

### 4. **Cosine Similarity**
   - The chatbot calculates the cosine similarity between the user input and predefined questions. The question with the highest similarity is chosen, and the corresponding response is returned.

### 5. **Response Generation**
   - After identifying the closest matching question, the chatbot responds with an appropriate message from the predefined responses for that category.

## Example Interaction

```text
Hello! I am a simple chatbot. Type 'exit' to end the conversation.
You: Hello
Bot: Hi there!
You: How are you?
Bot: I'm doing well, thank you!
You: What's your name?
Bot: I'm Bot, nice to meet you!
You: exit
Goodbye!
```

## File Structure

```text
simple-chatbot/
│
├── chatbot.py       # Main chatbot script
├── README.md        # Project README (this file)
└── requirements.txt # Python dependencies
```

## Customization

You can extend the chatbot by:
- **Adding new categories and responses**: Simply add more questions and their corresponding responses to the `data` and `responses` dictionaries.
- **Improving the NLP pipeline**: You can integrate more advanced NLP techniques like stemming or lemmatization for better input processing.
- **Expanding the dataset**: Add more sample questions to improve the bot's ability to understand a wide range of inputs.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
