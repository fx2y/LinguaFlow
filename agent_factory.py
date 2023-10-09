# Agent Factory
import re
import uuid

from communication_channel import CommunicationChannel
from llm_model import LLMModel


class AgentFactory:
    def __init__(self):
        self.agents = {}

    # Create new agent based on user's specifications
    def create_agent(self, name, personality, role, mode):
        # Check if agent name is unique and follows naming convention
        if not self._is_valid_name(name):
            return None

        # Check if agent personality is compatible with LLM model and task requirements
        if not self._is_compatible_personality(personality, mode):
            return None

        # Create new agent with unique ID and communication channel
        agent_id = self._generate_id()
        communication_channel = self._create_communication_channel(agent_id)

        # Configure agent's parameters based on mode
        from agent_configurator import AgentConfigurator
        agent_configurator = AgentConfigurator()
        if not agent_configurator.configure_agent(agent_id, mode):
            return None

        # Initialize agent's state based on role and task
        from agent_initializer import AgentInitializer
        agent_initializer = AgentInitializer()
        if not agent_initializer.initialize_agent(agent_id, role):
            return None

        # Register agent with Agent Manager and Communication Manager
        from agent_manager import AgentManager
        from communication_manager import CommunicationManager
        agent_manager = AgentManager()
        communication_manager = CommunicationManager()
        agent_manager.register_agent(agent_id, name, personality, role, mode)
        communication_manager.register_communication_channel(agent_id, communication_channel)

        # Add agent to list of agents
        self.agents[agent_id] = name

        return agent_id

    # Check if agent name is unique and follows naming convention
    def _is_valid_name(self, name):
        # Check if name is unique
        if name in self.agents.values():
            print("Error: Agent name is not unique.")
            return False

        # Check if name follows naming convention
        if not re.match(r'^[a-zA-Z0-9_-]+$', name):
            print("Error: Agent name does not follow naming convention.")
            return False

        return True

    # Check if agent personality is compatible with LLM model and task requirements
    def _is_compatible_personality(self, personality, mode):
        # Check if personality is compatible with LLM model and task requirements
        if not LLMModel.is_compatible_personality(personality, mode):
            print("Error: Agent personality is not compatible with LLM model and task requirements.")
            return False

        return True

    # Generate unique ID for agent
    def _generate_id(self):
        return uuid.uuid4()

    # Create communication channel for agent
    def _create_communication_channel(self, agent_id):
        return CommunicationChannel(agent_id)
