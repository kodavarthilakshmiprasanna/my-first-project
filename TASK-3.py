#  Chatbot with human

import random

print("Chatbot: Hello! Type 'bye' to exit.\n")

greetings = ["hi", "hello", "hey"]

greeting_responses = [
    "Hello, how can I help you?",
    "Hi, what can I do for you?",
    "Hey, how may I assist you?"
]

general_responses = [
    "That sounds interesting.",
    "I understand.",
    "Can you tell me more?",
    "I am here to help.",
    "That is good to hear."
]

# Random emojis list
emojis = ["😊", "👍", "✨", "🙂", "💡", "🚀"]

while True:
    user = input("You: ").lower().strip()

    if user == "bye":
        print("Chatbot: Goodbye", random.choice(emojis))
        break

    elif any(word in user for word in greetings):
        print("Chatbot:", random.choice(greeting_responses), random.choice(emojis))

    else:
        print("Chatbot:", random.choice(general_responses), random.choice(emojis))
