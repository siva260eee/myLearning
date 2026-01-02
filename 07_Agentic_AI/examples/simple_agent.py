# simple_agent.py

from src.agents.base_agent import BaseAgent
from src.tools.agent_tools import select_tool
from src.memory.agent_memory import AgentMemory
from src.planning.task_planner import TaskPlanner

class SimpleAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name)
        self.memory = AgentMemory()
        self.task_planner = TaskPlanner()

    def perform_task(self, task):
        tool = select_tool(task)
        self.memory.store(task)
        print(f"{self.name} is using {tool} to perform {task}.")
        # Simulate task execution
        self.memory.update(task, "completed")

if __name__ == "__main__":
    agent = SimpleAgent("Agent007")
    agent.perform_task("clean the room")