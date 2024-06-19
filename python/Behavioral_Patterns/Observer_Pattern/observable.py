from abc import ABC, abstractmethod

class AbstractObservable(ABC): 

    @abstractmethod 
    def add():
       """An abstract method""" 

    @abstractmethod 
    def remove():
       """An abstract method""" 

    @abstractmethod 
    def notify():
       """An abstract method""" 

class Observable(AbstractObservable):
    def __init__(self):
        self._observers=[] 
        self.tracked_value = 0
    
    def add(self, observer):
        if observer not in self._observers:
            self._observers.append(observer) 

    def remove(self,observer):
        try : 
            self._observers.remove(observer) 
        except ValueError:
            print(f"Error while removing the observer {observer}")

    def notify(self):
        for observer in self._observers:  
            observer.update()  
        
    '''
    def notify(self, modifier):
        for observer in self._observers:  
            if modifier != observer:  
                observer.update(self)  
    '''
    
    def update_tracked_value(self, new_val):
        self.tracked_value = new_val 
        self.notify()