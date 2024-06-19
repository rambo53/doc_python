from abc import ABC, abstractmethod
from monster import *
from obstacle import * 

class GameAbstractFactory(ABC):

    @abstractmethod 
    def get_monster():
       """An abstract method""" 
       

    @abstractmethod  
    def get_obstacle():
         """An abstract method"""  
     


class Level1Factory(GameAbstractFactory): 
    
    
    def get_monster(self):
      return MonsterLevel1()
    
    
    def get_obstacle(self):
      return ObstacleLevel1() 


class Level2Factory(GameAbstractFactory): 
    
     
    def get_monster(self):
      return MonsterLevel2()
    
    
    def get_obstacle(self):
      return ObstacleLevel2() 


class Level3Factory(GameAbstractFactory): 
    
   
    def get_monster(self):
      return MonsterLevel3()
    
     
    def get_obstacle(self):
      return ObstacleLevel3() 

class Level4Factory(GameAbstractFactory): 
    
     
    def get_monster(self):
      return MonsterLevel4()
   
     
    def get_obstacle(self):
      return ObstacleLevel4() 

