from abc import ABC, abstractmethod
from datetime import datetime



class AbstractMemento(ABC):
  
    @abstractmethod
    def get_value(self) -> str:
        pass
   

    @abstractmethod
    def get_date(self) -> str:
        pass


class Memento(AbstractMemento):
    def __init__(self, state_to_save: str) -> None:
        self._date = str(datetime.now())[:19]
        self._saved_state = state_to_save
        

    def get_value(self) -> str:
        return self._saved_state

    def get_date(self) -> str:
        return self._date