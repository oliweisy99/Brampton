class triangle:

    def __init__(self):
        self.a = 10
        self.h = 2

    def printArea(self):
        print(int(self.a * self.h) / 2)


class square:

    def __init__(self):
        self.a = 5
        self.b = 4

    def printArea(self):
        print(int(self.a * self.b))

obj = [triangle(), square(), square(), square(), triangle()]
for i in range(0, len(obj)):
    thing = obj[i]
    thing.printArea()
'''
s = square()
t = triangle()
s.printArea()
t.printArea()
'''