from abstract_state import State



class RealStateA(State):
    def transition_type_1(self) -> None:
        print("RealStateA handles request_1.")        
        self.context.transition_to(RealStateB())

    def transition_type_2(self) -> None:
        print("RealStateA handles request_2.")

    def transition_type_3(self) -> None:
        print("RealStateA handles request_3.")


class RealStateB(State):
    def transition_type_1(self) -> None:
        print("RealStateB handles request_1.")        
        

    def transition_type_2(self) -> None:
        print("RealStateB handles request_2.")
        self.context.transition_to(RealStateC())

    def transition_type_3(self) -> None:
        print("RealStateB handles request_3.")



class RealStateC(State):
    def transition_type_1(self) -> None:
        print("RealStateC handles request_1.")        
        

    def transition_type_2(self) -> None:
        print("RealStateC handles request_2.")

    def transition_type_3(self) -> None:
        print("RealStateC handles request_3.")
        self.context.transition_to(RealStateA())