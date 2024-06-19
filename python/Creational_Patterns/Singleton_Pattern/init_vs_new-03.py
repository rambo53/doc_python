class A : 
    def __init__(self,a):
        print("Run inside __init__ dunder ! ") 
        print(f"The a value = {a}")

    def __new__(cls, *args):
        print("Run inside __new__ dunder ! ") 
        return object.__new__(cls)


a= A(100)
