from abstract import AbstractClass

class Concrete2(AbstractClass):

    def mandatory_operations_1(self) -> None:
        print(f"{self.__class__.__name__} : Mandatory operation_1 : I'am doing a concrete things here !")

    def mandatory_operations_2(self) -> None:
        print(f"{self.__class__.__name__} : Mandatory operation_2 : I'am doing a concrete things here !")

    def mandatory_operations_3(self) -> None:
        print(f"{self.__class__.__name__} : Mandatory operation_3 : I'am doing a concrete things here !") 

'''   
    def operation_1(self) -> None:
        print(f"{self.__class__.__name__}: Message from base operation 1 inside the sub class . I'am doing something here")
'''        