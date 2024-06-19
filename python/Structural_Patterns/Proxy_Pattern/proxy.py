from service import * 
class Proxy(AbstractService):
    def __init__(self, real_service: AbstractService) -> None:
        self._real_service = real_service

    def run(self) -> None:
        if self.check():
            self._real_service.run()
            

    def check(self) -> bool:
        print("Checking for something")
        return True