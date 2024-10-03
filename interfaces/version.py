from abc import ABC, abstractmethod


class Version(ABC):

    @abstractmethod
    def generate(self) -> str:
        pass
