import json

class RuleBasedChatBot:
    def __init__(self, rules_path='chatbot/rules.json'):
        with open(rules_path, 'r') as file:
            self.rules = json.load(file)

    def get_response(self, message):
        message = message.lower()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "Sorry, I don't understand that."
