from abc import ABC, abstractmethod

class AbstractSortAlgorithm(ABC):

    @abstractmethod
    def sort(self, data):
        pass