from browsergym.experiment.loop import AbstractActionSet, DEFAULT_ACTION_SET, AgentArgs
from browsergym.experiment.agent import Agent
from dataclasses import dataclass


class CustomAgent(Agent):
    def __init__(self):
        # define which action set your agent will be using
        self.action_set = DEFAULT_ACTION_SET

    def obs_preprocessor(self, obs: dict) -> Any:
        # Optionally override this method to customize observation preprocessing
        # The output of this method will be fed to the get_action method and also saved on disk.
        # Example preprocessing logic
        # obs["custom_key"] = "custom_value"
        return super().obs_preprocessor(obs)

    def get_action(self, obs: Any) -> tuple[str, dict]:
        # Example implementation
        prompt = self.make_my_prompt_obs(obs)
        answer = self.llm(prompt)
        action, chain_of_thought = self.extract_action(answer)
        info = {
            "think": chain_of_thought,
            "messages": [prompt, answer],
            "stats": {"prompt_length": len(prompt), "answer_length": len(answer)},
            "some_other_info": "webagents are great",
        }
        return action, info


@dataclass
class CustomAgentArgs(AgentArgs):
    temperature: float = 0.5
    custom_param: str = "default_value"

    def make_agent(self) -> Agent:
        return CustomAgent(self.custom_param, self.temperature)