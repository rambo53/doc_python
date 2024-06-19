class MySingleton(object):
    _mysingleton_object = None

    @classmethod
    def get_instance(cls, a):
        if cls._mysingleton_object is None:
            print('Creating new object instance')
            cls._mysingleton_object = cls.__new__(cls)
            cls._mysingleton_object._my_init(a)
        return cls._mysingleton_object
     
    def __init__(self):
        raise RuntimeError('A call for get_instance() method is mandatory for instance creation!')

    
    
    def _my_init(self, param_a): 
        self.a = param_a 



o1 = MySingleton.get_instance(10)


o2 = MySingleton.get_instance(20)

print(f"o1.a = {o1.a} and o2.a = {o2.a}")

 

