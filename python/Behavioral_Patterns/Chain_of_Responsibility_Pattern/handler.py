from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class AbstractHandler(ABC): 

    _inner_handler: AbstractHandler = None

    def set_inner_handler(self, handler: AbstractHandler) -> AbstractHandler:
        self._inner_handler = handler     
        return handler
   
'''
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._inner_handler:
            return self._inner_handler.handle(request)
        return None
'''

 


class TypeAProductHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request in ["p1", "p2"]:
            return f"TypeAProductHandler manage {request}"
        else:
            if self._inner_handler:
                return self._inner_handler.handle(request)
            else :
                return None
              


class TypeBProductHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request in ["p3", "p4"]:
            return f"TypeBProductHandler manage {request}"
        else:
            if self._inner_handler:
                return self._inner_handler.handle(request)
            else :
                return None
             


class TypeCProductHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request in ["p5", "p6"]:
            return f"TypeCProductHandler manage {request}"
        else:
            if self._inner_handler:
                return self._inner_handler.handle(request)
            else :
                return None
             

class TypeDProductHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request in ["p7", "p8"]:
            return f"TypeDProductHandler manage {request}"
        else:
            if self._inner_handler:
                return self._inner_handler.handle(request)
            else :
                return None
            #return super().handle(request) 



