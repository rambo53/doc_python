class Visitor:
	"""Abstract visitor"""
	def __str__(self):
		return self.__class__.__name__


class LifeManager(Visitor):  
	def visit(self, monster):
		monster.manage_life(self)

    
class PowerManager(Visitor):  
	def visit(self, monster):
		monster.manage_power(self)   

