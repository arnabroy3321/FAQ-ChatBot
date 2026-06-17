import re
from responses import responses
from utils import clean_text

print("=" * 50)
print("College Help Desk Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    user_input = clean_text(user_input)

    if user_input == "exit":
        print("Bot: Thank you. Have a great day!")
        break

    found = False

    for pattern, answer in responses.items():

        if re.search(pattern, user_input):
            print("Bot:", answer)
            found = True
            break

    if not found:
        print("Bot: Sorry, I couldn't understand your question.")
        print("Bot: Please ask about admission, fees, hostel, courses, library, etc.")