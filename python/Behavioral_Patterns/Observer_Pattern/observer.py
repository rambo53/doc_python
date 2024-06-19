from abc import ABC, abstractmethod

class AbstractObserver(ABC): 

    @abstractmethod 
    def update():
       """An abstract method""" 


class Observer(AbstractObserver):
    def __init__(self, observable):
        self._observable = observable 
    
    def update(self):
        print(f"Updated value : {self._observable.tracked_value}")

