import random
import nltk

nltk.download('punkt')

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm here to help!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "Sorry, I don't have an answer for that."]
}

def chatbot_response(user_input):
    tokens= nltk.word_tokenize(user_input.lower())

    for word in tokens:
        if word in responses:
            return random.choice(responses[word])
    
    return random.choice(responses["default"])

print("Chatbot: Hi! Type 'bye' to end the chat")

while True:
    user_input= input("You: ")

    if user_input.lower()== "bye":
        print("Chatbot: Bye")
        break
    response= chatbot_response(user_input)
    print(f"Chatbot:{response}")