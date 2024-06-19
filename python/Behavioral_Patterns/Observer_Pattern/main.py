from observable import Observable
from observer import Observer


observable = Observable() 

observer_1 = Observer(observable) 
observer_2 = Observer(observable) 
observer_3 = Observer(observable) 
observer_4 = Observer(observable) 
observer_5 = Observer(observable) 

observable.add(observer_1)
observable.add(observer_2)
observable.add(observer_3)
observable.add(observer_4)
observable.add(observer_5)



observable.update_tracked_value(10) 

observable.remove(observer_2)

observable.update_tracked_value(20) 



