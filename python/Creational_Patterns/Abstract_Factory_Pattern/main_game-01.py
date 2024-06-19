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

 


def play_current_level( )->None: 
    """Here goes the code of the game main loop"""
    CURRENT_LEVEL = get_current_level()
    #...some code 
    #...more code 
    
    if CURRENT_LEVEL== 1 :
        m1 = MonsterLevel1() 
        o1 = ObstacleLevel1()
    elif CURRENT_LEVEL == 2: 
        m1 = MonsterLevel2() 
        o1 = ObstacleLevel2()
    elif CURRENT_LEVEL == 3: 
        m1 = MonsterLevel3() 
        o1 = ObstacleLevel3()
    else:
        m1 = MonsterLevel4() 
        o1 = ObstacleLevel4()
    
    m1.show() 
    o1.show() 

    #...more code 
    
    if CURRENT_LEVEL == 1 :
        m2 = MonsterLevel1() 
        o2 = ObstacleLevel1()
    elif CURRENT_LEVEL == 2: 
        m2 = MonsterLevel2() 
        o2 = ObstacleLevel2()
    elif CURRENT_LEVEL == 3: 
        m2 = MonsterLevel3() 
        o2 = ObstacleLevel3()
    else: 
        m2 = MonsterLevel4() 
        o2 = ObstacleLevel4()
    
    m2.show() 
    o2.show()

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
        print("##########   ", get_current_level(), " ##########")
        print(f"You are about playing  a game with the level {get_current_level()} ")        
        play_current_level()
        stay_playing = input("Do you went play a new game (yes/no ) ? ") 
        if stay_playing == "no" : 
            break 



main()
