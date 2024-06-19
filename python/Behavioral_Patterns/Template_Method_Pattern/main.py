from client import Client 
from concrete_1 import Concrete1
from concrete_2 import Concrete2 

client = Client() 

c1 = Concrete1()
client.play(c1) 

c2=Concrete2()
client.play(c2) 
 