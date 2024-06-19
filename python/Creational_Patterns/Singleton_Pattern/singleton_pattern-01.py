class MySingleton(object):
    _mysingleton_object = None

    @classmethod
    def get_instance(cls):
        if cls._mysingleton_object is None:
            print('Creating new object instance')
            cls._mysingleton_object = cls.__new__(cls)
        return cls._mysingleton_object
     
    def __init__(self):
        raise RuntimeError('A call for get_instance() method is mandatory for instance creation!')
'''
a1 = MySingleton()
print(a1)'''

 
a1 = MySingleton.get_instance()
print(a1)
 


a2 = MySingleton.get_instance()
print(a2)

 

print('Are they the same object?', a1 is a2)
 

