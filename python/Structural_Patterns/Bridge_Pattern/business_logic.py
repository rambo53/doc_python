from implementation import AbstractImplementation

class BusinessAbstraction:
 

    def __init__(self, implementation: AbstractImplementation) -> None:
        self.implementation = implementation

    def run(self) -> str:
        print(f"BusinessAbstraction: {self.implementation.run()}")


class ExtendedBusinessAbstraction(BusinessAbstraction):
   

    def run(self) -> str:
        print(f"ExtendedBusinessAbstraction: {self.implementation.run()}")

