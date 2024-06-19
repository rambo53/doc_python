class Product():
   

    def __init__(self) -> None:
        self.config_1 = None 
        self.config_2 = None 
        self.config_3 = None 



    def set_config(self, config_id, value) -> None:
        if config_id == 1 : 
            self.config_1 = value 
        elif config_id == 2 :
            self.config_2 = value 
        elif config_id == 3 :
            self.config_3 = value 
        else : pass 
    

 

    def show_all_config(self) -> None:
        print(f"Product config: config_1: {self.config_1} - config_2: {self.config_2} - config_3: {self.config_3}")
