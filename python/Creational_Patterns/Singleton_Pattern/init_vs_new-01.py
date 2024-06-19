class A : 
    def __init__(self):
        print("Run inside __init__ dunder ! ", self) 

        

    def __new__(cls):
        print("Run inside __new__ dunder ! ") 
        return object.__new__(cls)

a= A()
 