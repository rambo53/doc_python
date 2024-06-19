from target import Target


class App():
   

    def __init__(self, target: Target) -> None:
        self._mementos = []
        self._target = target

    def backup(self) -> None:
        print("App: Saving target")
        self._mementos.append(self._target.save())

    def undo(self) -> None:
        if len(self._mementos)==0:
            return

        last_memento = self._mementos.pop()
        print(f"App: Restoring.")
        try:
            self._target.restore(last_memento)
        except Exception:
            self.undo()

    def get_history(self) -> None:
        print("App: current mementos:")
        for memento in self._mementos:
            print(f"-->{memento.get_value()}")