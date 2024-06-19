from service import  RealService
from proxy import Proxy 

from client import Client



real_service = RealService()

client_1 = Client()
client_1.business_logic(real_service)


 
proxy = Proxy(real_service)
 
#client_2 = Client()
client_1.business_logic(proxy)
