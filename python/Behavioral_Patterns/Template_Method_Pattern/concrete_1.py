from abstract import AbstractClass

class Concrete1(AbstractClass):

    def mandatory_operations_1(self) -> None:
        print(f"{self.__class__.__name__} : Mandatory operation_1 : I'am doing a concrete things here !")

    def mandatory_operations_2(self) -> None:
        print(f"{self.__class__.__name__} : Mandatory operation_2 : I'am doing a concrete things here !")
    
    def mandatory_operations_3(self) -> None:
        print(f"{self.__class__.__name__} : Mandatory operation_3 : I'am doing a concrete things here !")