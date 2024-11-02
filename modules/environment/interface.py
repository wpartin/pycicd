from abc import ABC, abstractmethod


class Environment(ABC):

    @abstractmethod
    def init(self, *args) -> dict[str, str]:
        """Initialize your environment variables"""
        pass
