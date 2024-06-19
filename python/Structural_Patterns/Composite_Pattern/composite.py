from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class AbstractNode(ABC):
   

    @property
    def parent(self) -> AbstractNode:
        return self._parent

    @parent.setter
    def parent(self, parent: AbstractNode):     
        self._parent = parent

   

    def add(self, component: AbstractNode) -> None:
        pass

    def remove(self, component: AbstractNode) -> None:
        pass

    def is_node(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:  
        pass


class Leaf(AbstractNode):
    def operation(self) -> str:
        return "Leaf"


class Node(AbstractNode):

    def __init__(self) -> None:
        self._children: List[AbstractNode] = []

    def add(self, component: AbstractNode) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: AbstractNode) -> None:
        self._children.remove(component)
        component.parent = None

    def is_node(self) -> bool:
        return True

    def operation(self) -> str: 
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Node({'+'.join(results)})"
