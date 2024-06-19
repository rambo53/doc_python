from abc import ABC, abstractmethod
from receiver import Receiver

class AbstractCommand(ABC):
    """
    Abstract command.
    """
    @abstractmethod
    def run(self) -> None:
        """Abstract method"""
 


class Command_1(AbstractCommand):

    def __init__(self, attr: str) -> None:
        self._attr = attr

    def run(self) -> None:
        print(f"From command_1 {self._attr}") 


class Command_2(AbstractCommand):

    def __init__(self, receiver: Receiver, a: str, b: str, c: int) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b
        self._c = c

    def run(self) -> None:
        print("From command_2", end="")
        self._receiver.method_1(self._a)
        self._receiver.method_2(self._b, self._c)