import Sub_System.sub_system_classes as sub_sys 

class Facade : 
    def __init__(self) : 
        self.sub1 = sub_sys.SubSystem_1()
        self.sub2 = sub_sys.SubSystem_2()
        self.sub3 = sub_sys.SubSystem_3()
    
    def call_M_1(self): 
        RESULT = self.sub1.method_1() + ' ' + self.sub2.method_1() + ' ' + self.sub3.method_1() 
        return RESULT 
    
    def call_M_2(self): 
        RESULT = self.sub1.method_2() + ' ' + self.sub2.method_2() + ' ' + self.sub3.method_2() 
        return RESULT 


