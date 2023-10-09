from agent_manager import AgentManager


class AgentInitializer:
    def __init__(self):
        self.agent_manager = AgentManager()

    def initialize_agent(self, agent_id, role):
        # Initialize agent's state based on role and task
        if role == "task1":
            # TODO: Implement initialization for task1
            pass
        elif role == "task2":
            # TODO: Implement initialization for task2
            pass
        else:
            print("Error: Invalid role.")
            return False

        # Register agent with Agent Manager
        self.agent_manager.update_agent_state(agent_id, {"initialized": True})

        return True
