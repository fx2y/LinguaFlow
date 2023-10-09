from typing import Dict, Any, Optional

from agent_factory import AgentFactory


class AgentManager:
    def __init__(self):
        self.agents: Dict[str, Dict[str, Any]] = {}
        self.factory = AgentFactory()

    def create_agent(self, name: str, personality: str, role: str, mode: str, source: str) -> Optional[str]:
        agent_id = self.factory.create_agent(name, personality, role, mode, source)
        if agent_id is None:
            return None
        self.agents[agent_id] = {"name": name, "personality": personality, "role": role, "mode": mode, "source": source}
        return agent_id

    def get_agent_name(self, agent_id: str) -> Optional[str]:
        return self.agents.get(agent_id, {}).get("name")

    def get_all_agents(self) -> Dict[str, Dict[str, Any]]:
        return self.agents.copy()

    def update_agent_state(self, agent_id: str, state: Dict[str, Any]) -> None:
        if agent_id in self.agents:
            self.agents[agent_id].update(state)
        else:
            print(f"Error: Agent {agent_id} not found.")

    def register_agent(self, agent_id, name, personality, role, mode):
        self.agents[agent_id] = {
            'name': name,
            'personality': personality,
            'role': role,
            'mode': mode
        }
