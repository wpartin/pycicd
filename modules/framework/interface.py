from abc import ABC, abstractmethod


class Framework(ABC):

    @abstractmethod
    def __install(self) -> None:
        """Installs your framework"""
        pass

    @abstractmethod
    def run(self, directory: str) -> None:
        """Runs your implemented framework"""
        pass
