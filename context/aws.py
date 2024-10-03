from interfaces.context import Context
from models.definable_context_inputs import DefinableContextInputs
from typing import Dict, Any


class AwsContext(Context):

    def __init__(self, inputs: DefinableContextInputs):
        self.inputs = inputs

    def set(self, key: str, value: str) -> str:
        self.inputs[key] = value

        return self.inputs[key]

    def to_map(self) -> Dict[str, Any]:
        return {key: self.inputs.get(key) for key in self.inputs.key_set()}

    def __str__(self) -> str:
        return str(self.inputs)
