import json
from similarity import get_closest_faq

class Chatbot:
    def __init__(self):
        self.faqs = self.load_faqs()

    def load_faqs(self):
        with open('faq_data.json', 'r') as f:
            return json.load(f)

    def get_response(self, user_input):
        return get_closest_faq(user_input, self.faqs)