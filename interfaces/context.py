from abc import ABC, abstractmethod
from typing import Dict, Any


class Context(ABC):

    @abstractmethod
    def to_map(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
