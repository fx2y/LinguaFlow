import unittest
from unittest.mock import patch, MagicMock

from agent_factory import AgentFactory


class TestAgentFactory(unittest.TestCase):

    def setUp(self):
        self.agent_factory = AgentFactory()

    def test_create_agent(self):
        # Test creating a new agent with valid parameters
        agent_id = self.agent_factory.create_agent("test_agent", "friendly", "assistant", "training")
        self.assertIsNotNone(agent_id)
        self.assertIn(agent_id, self.agent_factory.agents.keys())

        # Test creating a new agent with invalid name
        agent_id = self.agent_factory.create_agent("invalid name", "friendly", "assistant", "training")
        self.assertIsNone(agent_id)

        # Test creating a new agent with invalid mode
        agent_id = self.agent_factory.create_agent("test_agent", "friendly", "assistant", "invalid_mode")
        self.assertIsNone(agent_id)

        # Test creating a new agent with invalid role
        agent_id = self.agent_factory.create_agent("test_agent", "friendly", "invalid_role", "training")
        self.assertIsNone(agent_id)

        # Test creating a new agent with invalid personality
        agent_id = self.agent_factory.create_agent("test_agent", "invalid_personality", "assistant", "training")
        self.assertIsNone(agent_id)

    def test_is_valid_name(self):
        # Test validating a unique and valid name
        self.assertTrue(self.agent_factory._is_valid_name("test_agent"))

        # Test validating a non-unique name
        self.agent_factory.agents = {1: "test_agent"}
        self.assertFalse(self.agent_factory._is_valid_name("test_agent"))

        # Test validating a name with invalid characters
        self.assertFalse(self.agent_factory._is_valid_name("test_agent!"))

    def test_generate_id(self):
        # Test generating a unique ID
        id1 = self.agent_factory._generate_id()
        id2 = self.agent_factory._generate_id()
        self.assertNotEqual(id1, id2)

    def test_create_communication_channel(self):
        # Test creating a communication channel
        agent_id = self.agent_factory._generate_id()
        communication_channel = self.agent_factory._create_communication_channel(agent_id)
        self.assertIsNotNone(communication_channel)

    @patch('agent_configurator.AgentConfigurator.configure_agent')
    @patch('agent_initializer.AgentInitializer.initialize_agent')
    @patch('agent_manager.AgentManager.create_agent')
    @patch('communication_manager.CommunicationManager.register_communication_channel')
    def test_create_agent_with_mock(self, mock_register_communication_channel, mock_create_agent, mock_initialize_agent,
                                    mock_configure_agent):
        # Test creating a new agent with valid parameters
        mock_configure_agent.return_value = True
        mock_initialize_agent.return_value = True
        agent_id = self.agent_factory.create_agent("test_agent", "friendly", "assistant", "training")
        self.assertIsNotNone(agent_id)
        self.assertIn(agent_id, self.agent_factory.agents.keys())
        mock_configure_agent.assert_called_once_with(agent_id, "training")
        mock_initialize_agent.assert_called_once_with(agent_id, "assistant")
        mock_create_agent.assert_called_once_with(agent_id, "test_agent", "friendly", "assistant", "training")
        mock_register_communication_channel.assert_called_once_with(agent_id, MagicMock())


if __name__ == '__main__':
    unittest.main()
