from __future__ import annotations
from abc import ABC, abstractmethod

from product import Product


class Builder(ABC):
  
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_config_1(self) -> None:
        pass

    @abstractmethod
    def produce_config_2(self) -> None:
        pass

    @abstractmethod
    def produce_config_3(self) -> None:
        pass


class ConcreteBuilder(Builder):
  

    def __init__(self) -> None:
      
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
      
        
        product = self._product
        self.reset()
        return product

    def produce_config_1(self) -> None:
        self._product.set_config(1, "val1") 

    def produce_config_2(self) -> None:
        self._product.set_config(2, "val2") 

    def produce_config_3(self) -> None:
        self._product.set_config(3, "val3") 

    
    def build_setting_A(self)->None:
        self.produce_config_1()
        self.produce_config_2()

    def build_setting_B(self)->None:
        self.produce_config_1()
        self.produce_config_3()
        