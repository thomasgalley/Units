class Amount:
    def __init__(self,quantity='',unit='',coefficient=0):
        self.quantity=quantity
        self.unit=unit
        self.coefficient=coefficient
    def convert(self,conversionunit):
        if self.unit==conversionunit:
            return self.coefficient
        if self.unit=='meters' and conversionunit=='kilometers':
            return 0.001*self.coefficient
        elif self.unit=='kilometers' and conversionunit=='meters':
            return 1000*self.coefficient
        if self.unit=='seconds' and conversionunit=='minutes':
            return 0.016666666666666666666666666666667*self.coefficient
        if self.unit=='minutes' and conversionunit=='seconds':
            return 60*self.coefficient
        else:
            raise TypeError('Incomparibleunits') 
    def add(self, others):
            if self.quantity==others.quantity:
                if self.unit==others.unit:
                    return self.coefficient+others.coefficient
                else:
                    return others.coefficient+self.convert(others.unit)     
            else:
                 raise TypeError('Incompatibleunits')
                 return
    def multiply(self,others):
            if self.quantity==others.quantity:
                if self.unit==others.unit:
                    return self.coefficient*others.coefficient
                else:
                    return self.coefficient*others.coefficient  
            else:
                return self.coefficient*others.coefficient  
    def __str__(self):
        return str(self.coefficient)+'*'+self.unit
    def __add__(self, other):
        return str(self.add(other))+'*'+other.unit
    def __eq__(self,other):
        if self.quantity==other.quantity:
            if self.unit==other.unit:
                if self.coefficient==other.coefficient:
                    return True
                else:
                    return False
            else:
                if other.coefficient==self.convert(other.unit):
                        return True
                else:
                    return False
        else:
            raise TypeError('Incompatibleunits')
  


