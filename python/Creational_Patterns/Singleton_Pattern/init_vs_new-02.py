class A : 
    def __init__(self):
        print("Run inside __init__ dunder ! ") 
        print(f"Params: {self}")

    def __new__(cls):
        print("Run inside __new__ dunder ! ") 
        print(f"Params: {cls}")
        return object.__new__(cls)


a= A()
