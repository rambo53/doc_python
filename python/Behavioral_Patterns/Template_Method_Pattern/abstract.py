from abc import ABC, abstractmethod


class AbstractClass(ABC):
   

    def template_method(self) -> None:
        
        self.operation_1()
        self.mandatory_operations_1()
        self.operation_2()
        self.mandatory_operations_2()
        self.operation_3()
        self.mandatory_operations_3()


    def operation_1(self) -> None:
        print(f"{self.__class__.__name__}: Message from base operation 1. I'am doing something here")

    def operation_2(self) -> None:
        print(f"{self.__class__.__name__}: Message from base operation 2. I'am doing something here")

    def operation_3(self) -> None:
        print(f"{self.__class__.__name__}: Message from base operation 3. I'am doing something here")

     

    @abstractmethod
    def mandatory_operations_1(self) -> None:
        pass

    @abstractmethod
    def mandatory_operations_2(self) -> None:
        pass

    @abstractmethod
    def mandatory_operations_3(self) -> None:
        pass

  

  