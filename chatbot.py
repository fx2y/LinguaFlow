class Chatbot:
    def __init__(self):
        self.name = "Chatbot"
        self.greeting = "Hello! How can I assist you today?"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_greeting(self):
        return self.greeting

    def set_greeting(self, greeting):
        self.greeting = greeting

    def respond(self, message):
        # Implement your chatbot's response logic here
        # ...
        return "I'm sorry, I don't understand. Can you please rephrase?"
