from abc import ABC, abstractmethod


class Runner(ABC):

    @abstractmethod
    def run(self, command: list[str], environment: dict[str, str]) -> None:
        """Implement a run pattern"""
        pass
