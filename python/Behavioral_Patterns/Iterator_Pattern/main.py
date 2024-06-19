from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

 


class  AlternateIterator(Iterator):
    
    _next_left_position: int = 0
    _next_right_position:int = 0
 

    def __init__(self, data) -> None:
        if data is not None :
            self._data = data
            self._next_left_position=0
            self._next_right_position=len(data)-1
            self._left_side=True
            if self._next_right_position < 0 : 
                self._next_right_position = 0
            
        
      
       

    def __next__(self):
       
      
        try:
            
            if self._next_left_position > self._next_right_position :
                raise StopIteration()
            if self._left_side :
                value = self._data[self._next_left_position]
                self._left_side=False
                self._next_left_position+=1
            else: 
                value = self._data[self._next_right_position]
                self._left_side=True
                self._next_right_position-=1

        except IndexError:
            raise StopIteration()

        return value


class IterableData(Iterable):
    
    def __init__(self, collection: List[Any] = []) -> None:
         self._collection = collection

    def __iter__(self) -> AlternateIterator:
        
        return AlternateIterator(self._collection)
    
    def add_item(self, item: Any):
        self._collection.append(item)


container = IterableData()
for i in range(0,100):
    container.add_item(str(i))

print("traverse all items:")

print("\n".join(container))
   

   

