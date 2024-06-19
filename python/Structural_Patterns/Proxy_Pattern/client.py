from service import AbstractService
 

class Client:
   
    # client code

    def business_logic(self, an_object:AbstractService):
        #Client operations
        an_object.run()
        #Other client operations

    # Other client code