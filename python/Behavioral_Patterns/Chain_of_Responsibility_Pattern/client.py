from handler import AbstractHandler

class Client:
    def work_on(self, handler:AbstractHandler,  list_of_products: list)->None:
        for item in list_of_products:
            print(f"Client: asking for handler for {item}.")
            result = handler.handle(item)
            if result:
                print(result)
            else:
                print(f"There is no handler for {item}")
