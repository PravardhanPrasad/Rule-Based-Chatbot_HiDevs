import pytest
from chatbot.bot import RuleBasedChatBot

@pytest.fixture
def bot():
    return RuleBasedChatBot()

def test_greeting(bot):
    assert bot.get_response("hello") == "Hi there!"

def test_name_question(bot):
    assert bot.get_response("what's your name") == "I'm a rule-based chatbot."

def test_unknown_input(bot):
    assert bot.get_response("what's the weather today?") == "Sorry, I don't understand that."
