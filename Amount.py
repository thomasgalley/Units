class Amount:
    def __init__(self,quantity='',unit='',coefficient=0):
        self.quantity=quantity
        self.unit=unit
        self.coefficient=coefficient
    def add(self, others):
            if self.quantity==others.quantity:
                if self.unit==others.unit:
                    return self.coefficient+others.coefficient
            else:
                raise ValueError('Incompatibleunits')
    def convert(self,conversionunit):
        if self.unit=='meter' and conversionunit=='kilometer':
            return 0.001*self.coefficient
        elif self.unit=='kilometer' and conversionunit=='meter':
            return 1000*self.coefficient
        else:
            return self.coefficient
    def test(self,t=0):
        return self.coefficient*t
