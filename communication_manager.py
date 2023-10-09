# Communication Manager
class CommunicationManager:
    def __init__(self):
        self.communication_channels = {}

    # Register communication channel for agent
    def register_communication_channel(self, agent_id, communication_channel):
        self.communication_channels[agent_id] = communication_channel

    # Get communication channel for agent
    def get_communication_channel(self, agent_id):
        return self.communication_channels.get(agent_id, None)
