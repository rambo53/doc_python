from class_a import ClassA
from class_b import ClassB


class Adapter(ClassA, ClassB):
    def method_1(self, message : str) -> None:
        print("Adapter: run the non adapted methode_2 after calling method_1 !")
        self.method_2(message)
