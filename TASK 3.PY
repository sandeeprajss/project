import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only required once)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me ChatGPT!", "I'm your friendly chatbot. What's your name?"]
    ],
    [
        r"how are you?",
        ["I'm just a program, so I don't have feelings, but thanks for asking!", "I'm doing great! How about you?"]
    ],
    [
        r"what can you do?",
        ["I can answer your questions, provide information, or just chat with you!", "I'm here to help you with your queries."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! See you soon!"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I assist you today?", "Hello, %1! What can I do for you?"]
    ],
    [
        r"what is (.*)",
        ["I'm not sure about %1, but I can look it up for you!", "Hmm, I don't know about %1. Can you tell me more?"]
    ],
    [
        r"how old are you?",
        ["I'm just a program, so I don't have an age!", "Age is just a number for me. I'm timeless!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye! See you soon!"]
    ]
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chat():
    print("Chatbot: Hello! I'm your AI chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()