from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):

    @abstractmethod
    def parse(self, *args) -> Any:
        """An abstract method to parse over something."""
        pass
