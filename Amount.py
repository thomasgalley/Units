class Amount:
	def __init__(self,quantity='',unit='',coefficient=0):
		self.quantity=quantity
		self.unit=unit
		self.coefficient=coefficient
	def metertocentimetre(self):
            if self.quantity=='length': 
                if self.unit=='metre':
                    self.coefficient=100*self.coefficient
	def printcoeff(self):
         print(self.coefficient)
	def add(self, others):
            if self.quantity==others.quantity:
                if self.unit==others.unit:
                    return self.coefficient+others.coefficient
