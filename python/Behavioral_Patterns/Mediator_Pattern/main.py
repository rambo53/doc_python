from base_classes import * 


o1 = ConcretClassA()
o2 = ConcretClassB()
mediator = Mediator(o1, o2)

print("Client run work_on_a of ConcretClassA.")
o1.work_on_a()

print("Client run work_on_c of ConcretClassB.")
o2.work_on_c()