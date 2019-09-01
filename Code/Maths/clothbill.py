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

    def __str__(self):
            return '%-10s Pants'%(self.colour)

    def getcost(self):
            return self.rate * self.size + self.labour

class shirt(clothing):
    def __init__(self, cloth, size, labour):
            self.labour = labour
            self.size = size
            clothing.__init__(self,cloth.colour, cloth.rate)

    def __str__(self):
            return '%-10s Shirt'%(self.colour)

    def getcost(self):
            return self.rate * self.size + self.labour


cheapblue = clothing('blue', 20.0)
costlyred = clothing('red', 100.0)

items = []
items.append(pants(cheapblue, 2.0, 150.0) )
items.append(shirt(costlyred, 1.5, 130.0) )

for k in items:
    print( k, k.getcost())
