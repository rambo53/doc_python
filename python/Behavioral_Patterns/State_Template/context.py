from abstract_state import State


class Context:
    

    _internal_state = None
    

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):

        print(f"Transition to {type(state).__name__} state")
        self._internal_state = state
        self._internal_state.context = self

   

    def request_1(self):
        self._internal_state.transition_type_1()

    def request_2(self):
        self._internal_state.transition_type_2()
    
    def request_3(self):
        self._internal_state.transition_type_3()
