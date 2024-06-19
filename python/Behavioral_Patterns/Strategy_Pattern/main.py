 
 
import random
from Algorithms.abstract_algorithm import AbstractSortAlgorithm
from Algorithms.min_sort import MinSort
from Algorithms.bubble_sort import BubbleSort
 
from business_logic import BusinessClass


def get_random_list():
    n=20
    data=[]
    for i in range(1,n) : 
        data.append(random.randint(0,1000))

    return data


data_1 = get_random_list()


data_2=data_1.copy()



business_logic = BusinessClass(MinSort())
business_logic.business_logic_operations(data_1)

 
 
business_logic.strategy = BubbleSort()
business_logic.business_logic_operations(data_2)  
 
