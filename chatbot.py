#  My project is Rule-Based AI Chatbot project -1
# DecodeLabs - Artificial Intelligence Project -1

# Knowledge base containing 5+ predefined intents
responses = {
    "greeting": "Hello! 👋 Welcome to the Rule-Based AI Chatbot. How can I help you?",
    "name": "I am a simple rule-based AI chatbot created for DecodeLabs Project 1.",
    "how_are_you": "I'm doing great! Thanks for asking me. 😊",
    "help": "I can respond to greetings, tell you about myself, explain what I can do, and say goodbye.",
    "capabilities": "I can handle predefined user inputs using rules, dictionaries, if-else logic, and a continuous loop.",
    "thanks": "You're welcome! 😊",
    "creator": "I was created as part of an Artificial Intelligence Project 1 by Sk.Farhan.",
    "goodbye": "Goodbye! 👋 Have a great day! tata"
}


# It is for Mapping different user inputs to predefined intents
input_to_intent = {
    "hello": "greeting",
    "hi": "greeting",
    "hey": "greeting",
    "good morning": "greeting",
    "good afternoon": "greeting",
    "good evening": "greeting",

    "what is your name": "name",
    "what's your name": "name",
    "who are you": "name",

    "how are you": "how_are_you",
    "how are you doing": "how_are_you",

    "help": "help",
    "help me": "help",

    "what can you do": "capabilities",
    "your capabilities": "capabilities",
    "what do you do": "capabilities",

    "thanks": "thanks",
    "thank you": "thanks",

    "who created you": "creator",
    "who made you": "creator"
}


# The Commands that terminate the chatbot
exit_commands = {
    "bye",
    "goodbye",
    "exit",
    "quit"
}


def chatbot():
    """Run the rule-based chatbot."""

    print("=" * 55)
    print("        RULE-BASED AI CHATBOT 🤖")
    print("=" * 55)
    print("Type 'hello' to start chatting.")
    print("Type 'help' to see what I can do.")
    print("Type 'exit', 'quit', 'bye', or 'goodbye' to stop.")
    print("=" * 55)

    # IT IS -->Continuous interaction loop
    while True:
        raw_input = input("\nYou: ")

        # FOR Input sanitization: remove extra whitespace and ignore case
        user_input = raw_input.lower().strip()

        # The Handle empty input
        if not user_input:
            print("Bot: Please enter a message.")
            continue

        # The Exit strategy
        if user_input in exit_commands:
            print("Bot:", responses["goodbye"])
            break

        # This is Rule-based response using if-else logic
        elif user_input in input_to_intent:
            intent = input_to_intent[user_input]
            print("Bot:", responses[intent])

        #  TO GET of Fallback for unknown inputs
        else:
            print(
                "Bot: I'm sorry, I don't understand that yet. "
                "Please try a predefined command or type it 'help'."
            )


# To Start the chatbot
if __name__ == "__main__":
    chatbot()
