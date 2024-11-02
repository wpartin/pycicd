from abc import ABC, abstractmethod


class Login(ABC):

    @abstractmethod
    def login(self, *args) -> None:
        """Allows you to implement a login method for your implementation"""
        pass
