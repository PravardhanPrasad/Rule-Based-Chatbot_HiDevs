from chatbot.bot import RuleBasedChatBot

def main():
    bot = RuleBasedChatBot()
    print("ChatBot: Hello! Type something or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("ChatBot: Bye!")
            break
        response = bot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
