import random
from abstract_factory import * 

CURRENT_LEVEL_FROM_DB= 1 
MAX_LEVEL = 4




def get_current_level():    
    return CURRENT_LEVEL_FROM_DB #Supposed to be read from a database


def go_to_next_level():
    global CURRENT_LEVEL_FROM_DB
    CURRENT_LEVEL_FROM_DB = CURRENT_LEVEL_FROM_DB+1 #Supposed to update the CURRENT_LEVEL into a database
    if CURRENT_LEVEL_FROM_DB > MAX_LEVEL : 
        CURRENT_LEVEL_FROM_DB=1

def get_factory()->GameAbstractFactory : 
    factories={
        1:Level1Factory(),
        2:Level2Factory(),
        3:Level3Factory(),
        4:Level4Factory()
    }
    
    CURRENT_LEVEL = get_current_level() 
    return factories[CURRENT_LEVEL] 


def play_current_level(current_factory)->None: 
    """Here goes the code of the game main loop"""
    
    #...game code 
    #...more code 

    m1 = current_factory.get_monster() 
    o1 = current_factory.get_obstacle()
    m1.show() 
    o1.show()

    #...more code again  
    #...more code again and again 
    passed_level = random.randint(0,1)
    if passed_level  == 1 :
        print("Pass to the next level :-)")
        go_to_next_level() 
    else :
        print("Stay in current level :-(")



     
    
def main()->None:
    while True :
        print(f"You are about playing  a game with the level {get_current_level()} ")
        current_factory = get_factory()
        play_current_level(current_factory)
        stay_playing = input("Keep playing (yes/no ) ? ") 
        if stay_playing == "no" : 
            break 



main()
