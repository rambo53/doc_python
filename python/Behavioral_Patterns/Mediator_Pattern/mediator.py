from __future__ import annotations
from abc import ABC
from base_classes import *

class AbstractMediator(ABC):
  def notify(self, sender: object, event: str) -> None:
    """Abstract class"""
      


class Mediator(AbstractMediator):
    def __init__(self, o1: ConcretClassA, o2: ConcretClassB) -> None:
        self._o1 = o1
        self._o1.mediator = self
        self._o2 = o2
        self._o2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "Event_1":
            print("Mediator recting on Event_1:")
            self._o2.work_on_d()
        elif event == "Event_2":
            print("Mediator recting on Event_2:")
            self._o1.work_on_b()
        else:
            print("Mediator: do something else... without firing additional event")