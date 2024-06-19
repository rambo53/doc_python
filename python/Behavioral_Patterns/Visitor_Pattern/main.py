from monster import Monster
from visitor import * 



visitor_1 = LifeManager()
visitor_2 = PowerManager() 

monster_1 = Monster() 
monster_1.accept(visitor_1) 
monster_1.accept(visitor_2) 

monster_2 = Monster() 
monster_2.accept(visitor_1) 
monster_2.accept(visitor_2) 

