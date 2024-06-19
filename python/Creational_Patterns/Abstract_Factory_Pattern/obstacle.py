from abc import ABC, abstractmethod

class Obstacle(ABC) :
    
    @abstractmethod 
    def show():
        """An abstract method"""
        

class ObstacleLevel1(Obstacle):
    def show(self):
        print("I'am an obstacle from level 1")

class ObstacleLevel2(Obstacle):
    def show(self):
        print("I'am an obstacle from level 2")

class ObstacleLevel3(Obstacle):
    def show(self):
        print("I'am an obstacle from level 3")

class ObstacleLevel4(Obstacle):
    def show(self):
        print("I'am an obstacle from level 4")



