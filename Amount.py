class Amount:
    def __init__(self,quantity='',unit='',coefficient=0):
        self.quantity=quantity
        self.unit=unit
        self.coefficient=coefficient
    def convert(self,conversionunit):
        if self.unit==conversionunit:
            return self.coefficient
        if self.unit=='meter' and conversionunit=='kilometer':
            return 0.001*self.coefficient
        elif self.unit=='kilometer' and conversionunit=='meter':
            return 1000*self.coefficient
        if self.unit=='second' and conversionunit=='hour':
            return 0.016666666666666666666666666666667*self.coefficient
        if self.unit=='hour' and conversionunit=='second':
            return 60*self.coefficient
        else:
            return self.coefficient
    def add(self, others):
            if self.quantity==others.quantity:
                if self.unit==others.unit:
                    return self.coefficient+others.coefficient
                else:
                    return others.coefficient+self.convert(others.unit)     
            else:
                raise ValueError('Incompatibleunits')
    def test(self,t=0):
        return self.coefficient*t
