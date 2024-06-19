from command import AbstractCommand

class Invoker:
    def __init__(self, on_start=None, on_finish=None):
        self._on_start =  on_start
        self._on_finish = on_finish

    

    def do_something(self) -> None:
        print("From Invoker: Maybe execute something before starting my job ?")
        if isinstance(self._on_start, AbstractCommand):
            self._on_start.run()

        print("From Invoker: Doing my job !")

        print("From Invoker: Maybe execute something after ending my job ?")
        if isinstance(self._on_finish, AbstractCommand):
            self._on_finish.run()
