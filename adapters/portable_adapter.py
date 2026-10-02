from abc import ABC, abstractmethod
from typing import Any

class AgentAdapter(ABC):
    framework_name="framework-independent"
    @abstractmethod
    def manifest(self, agent): ...
    @abstractmethod
    def invoke(self, agent, tool_name: str, inputs: dict[str, Any]): ...

class OpenAIAdapter(AgentAdapter):
    framework_name="OpenAI SDK"
    def manifest(self, agent): return {"framework":self.framework_name,"tools":agent.tools()}
    def invoke(self, agent, tool_name, inputs): return agent.run(tool_name,inputs)

class CrewAIAdapter(AgentAdapter):
    framework_name="CrewAI"
    def manifest(self, agent): return {"framework":self.framework_name,"tools":agent.tools()}
    def invoke(self, agent, tool_name, inputs): return agent.run(tool_name,inputs)

class ClaudeCodeAdapter(AgentAdapter):
    framework_name="Claude Code"
    def manifest(self, agent): return {"framework":self.framework_name,"tools":agent.tools()}
    def invoke(self, agent, tool_name, inputs): return agent.run(tool_name,inputs)

class LyzrAdapter(AgentAdapter):
    framework_name="Lyzr"
    def manifest(self, agent): return {"framework":self.framework_name,"tools":agent.tools()}
    def invoke(self, agent, tool_name, inputs): return agent.run(tool_name,inputs)
