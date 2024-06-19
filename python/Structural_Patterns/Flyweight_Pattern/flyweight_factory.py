from typing import Dict


from flyweight import Flyweight


class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: list) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: list) -> str:
        key = "-".join(state)
        return key

    def get_flyweight(self, _shared_object: list) -> Flyweight:
        key = self.get_key(_shared_object)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Creating new flyweight object.")
            self._flyweights[key] = Flyweight(_shared_object)
        else:
            print("FlyweightFactory: A shared flyweight exist.")

        return self._flyweights[key]

    def show_existing_flyweights(self) -> None:
        print(f"FlyweightFactory: There is {len(self._flyweights)} existing flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")