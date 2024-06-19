from abc import ABC, abstractmethod

class Monster(ABC) :
    
    @abstractmethod 
    def show():
        """An abstract method"""  

class MonsterLevel1(Monster):
    def show(self):
        print("I'am a Monster from level 1")

class MonsterLevel2(Monster):
    def show(self):
        print("I'am a Monster from level 2")

class MonsterLevel3(Monster):
    def show(self):
        print("I'am a Monster from level 3")

class MonsterLevel4(Monster):
    def show(self):
        print("I'am a Monster from level 4")


 
