from memento import *
import random


class Target():
    _state = None
    def __init__(self) -> None:
        self._state = random.randint(1,1000)
        print(f"Target: initial value is: {self._state}")

    def run(self) -> None:
        #Some code.
        self._state = random.randint(1,1000)
        print(f"Target: generated value: {self._state}")

    

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_value()
        print(f"Target: restore the value: {self._state}")


