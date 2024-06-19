from abc import ABC, abstractmethod
 


class State(ABC):


    @property
    def context(self) :
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def transition_type_1(self) -> None:
        """Abstract method"""

    @abstractmethod
    def transition_type_2(self) -> None:
        """Abstract method"""

 
    @abstractmethod
    def transition_type_3(self) -> None:
        """Abstract method"""