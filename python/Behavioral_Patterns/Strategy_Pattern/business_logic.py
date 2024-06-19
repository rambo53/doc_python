import time
from Algorithms.abstract_algorithm import AbstractSortAlgorithm

class BusinessClass : 
    def __init__(self, strategy) : 
        self._strategy = strategy 
        
    
    @property
    def strategy(self):
        return self._strategy 

    @strategy.setter
    def strategy(self, strategy: AbstractSortAlgorithm) -> None: 
        self._strategy = strategy


    def business_logic_operations(self, data) -> None:
        print("===================================================") 
        print(f"The current sorting strategy {self._strategy}.")

        start = time.time()
        result = self._strategy.sort(data)
        end = time.time()
        elapsed = end - start

        print(f'Run time : {elapsed:.2}ms')

        #print(f"After application of the current strategy : {list(result)}")
        
