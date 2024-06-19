class Base_Class : 
    def get_name(self):
        return "#"


class Base_class_Decorator(Base_Class):
    def __init__(self, base_class_object):
        self.base_class_object = base_class_object

    def get_name(self):
        
        return self.base_class_object.get_name() + " # "


o1 = Base_Class()
 

o2 = Base_class_Decorator(o1)
 

o3 = Base_class_Decorator(o2)
print(o3.get_name())
