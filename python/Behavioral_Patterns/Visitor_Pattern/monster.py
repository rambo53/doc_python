class Monster():

 

    def accept(self, visitor):
        visitor.visit(self) 
    
    def manage_life(self, life_manager):
        print(f"Use {life_manager} to manage the {self} remaning life")
        

    def manage_power(self, power_manager):
        print(f"Use {power_manager} to manage the {self} power")
 
    def __str__(self):
        return self.__class__.__name__
