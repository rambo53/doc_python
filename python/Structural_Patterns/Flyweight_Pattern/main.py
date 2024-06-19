 
from flyweight_factory import FlyweightFactory

 


flyweight_factory = FlyweightFactory([
    ["product_A", "attr_A_1", "attr_A_2"],
    ["product_B", "attr_B_1", "attr_B_2"],
    ["product_C", "attr_C_1", "attr_C_2"],
    ["product_D", "attr_D_1", "attr_D_2"]
])

flyweight_factory.show_existing_flyweights()
print("\n")

o1= ["product_B", "attr_B_1", "attr_B_2"]
print(f"adding the object {o1}")
flyweight_factory.get_flyweight(o1)

print("\n")
flyweight_factory.show_existing_flyweights()

print("\n")
o2= ["product_E", "attr_E_1", "attr_E_2"]
print(f"adding the object {o2}")
flyweight_factory.get_flyweight(o2)

print("\n")
flyweight_factory.show_existing_flyweights()


