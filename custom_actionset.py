from browsergym.core.action.base import AbstractActionSet
from browsergym.core.action.highlevel import HighLevelActionSet

class CustomActionSet(AbstractActionSet):
    def describe(self, with_long_description: bool = True, with_examples: bool = True) -> str:
        return "Custom action set description."

    def example_action(self, abstract: bool) -> str:
        return "Example actions for in context learning."

    def to_python_code(self, action) -> str:
        return "executable python code"
    
highLevelAction = HighLevelActionSet()
print(highLevelAction.example_action())