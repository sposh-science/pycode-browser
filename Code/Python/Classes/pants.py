class clothing:
    def __init__(self,colour, rate):
            self.colour = colour
            self.rate = rate

    def getcolour(self):
            return self.colour

    def __str__(self):
            return '%s Cloth at Rs. %6.2f per sqmtr'%(self.colour, self.rate)

class pants(clothing):
    def __init__(self, cloth, size, labour):
            self.labour = labour
            self.size = size
            clothing.__init__(self,cloth.colour, cloth.rate)

    def getcost(self):
            return self.rate * self.size + self.labour

costlyred = clothing('red', 100.0)
smallpant = pants(costlyred, 1.5, 100)
print  smallpant.getcost()
print smallpant