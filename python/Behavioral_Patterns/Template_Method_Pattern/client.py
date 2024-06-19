from abstract import AbstractClass


class Client : 
    def play(self, object_with_template_method: AbstractClass)->None :
        object_with_template_method.template_method()

