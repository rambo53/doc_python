 
import random 

class MySingleton(object):
    _mysingleton_object = None

    
    def __new__(cls):
        if cls._mysingleton_object is None:
            print('Creating new object instance')
            cls._mysingleton_object =  super(MySingleton, cls).__new__(cls)
        return cls._mysingleton_object
    def __init__(self):
        self.a= random.randint(0,1000)

o1 = MySingleton()
print(f"{o1.a}")

o2 = MySingleton()
print(f"{o2.a}") 

print(f"{o1.a}")