# Communication Channel
class CommunicationChannel:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.messages = []

    # Send a message to the communication channel
    def send_message(self, message):
        self.messages.append(message)

    # Receive a message from the communication channel
    def receive_message(self):
        if len(self.messages) > 0:
            return self.messages.pop(0)
        else:
            return None
