 

class Observable( ):
    def __init__(self):
       
        self.tracked_value = 0 
    
    def update_tracked_value(self, new_val):
        self.tracked_value = new_val 
      