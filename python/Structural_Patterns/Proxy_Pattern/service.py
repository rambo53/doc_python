from abc import ABC, abstractmethod


class AbstractService(ABC):
     
    @abstractmethod
    def run(self) -> None:
        pass


class RealService(AbstractService):
   

    def run(self) -> None:
        print("Do something.")