from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractImplementation(ABC):
   

    @abstractmethod
    def run(self) -> str:
        """Abstract method"""




class ConcreteImplementation1(AbstractImplementation):
    def run(self) -> str:
        print("ConcreteImplementationA: do something.")
        return "ok"


class ConcreteImplementation2(AbstractImplementation):
    def run(self) -> str:
        print("ConcreteImplementationB: do something.")
        return "ok"