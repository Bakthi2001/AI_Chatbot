from preprocess import preprocess_text
from chatbot import Chatbot

# Initialize the chatbot
chatbot = Chatbot()

print("Welcome to the Customer Support Chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chatbot.get_response(user_input)
    print("Bot: " + response)