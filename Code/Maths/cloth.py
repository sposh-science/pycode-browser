class clothing:
    def __init__(self,colour, rate):
            self.colour = colour
            self.rate = rate

    def getcolour(self):
             return self.colour
                                
cheapblue = clothing('blue', 20.0)
costlyred = clothing('red', 100.0)
print cheapblue.rate
print costlyred