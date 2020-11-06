class clothing:
    def __init__(self,colour, rate):
            self.colour = colour
            self.rate = rate

    def getcolour(self):
            return self.colour

    def __str__(self):
            return '%s Cloth at Rs. %6.2f per sqmtr'%(self.colour, self.rate)
cheapblue = clothing('blue', 20.0)
costlyred = clothing('red', 100.0)
print( cheapblue.rate)
print( costlyred)