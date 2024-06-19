
from __future__ import annotations
from mediator import Mediator


class AbstractClass:
 

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator




class ConcretClassA(AbstractClass):
    def work_on_a(self) -> None:
        print("ConcretClassA work on A.")
        #Do something and...
        self.mediator.notify(self, "Event_1")

    def work_on_b(self) -> None:
        print("ConcretClassA work on B.")
        self.mediator.notify(self, "Event_3")


class ConcretClassB(AbstractClass):
    def work_on_c(self) -> None:
        print("ConcretClassB work on C.")
        #Do something and...
        self.mediator.notify(self, "Event_2")

    def work_on_d(self) -> None:
        print("ConcretClassB work on D.")
       