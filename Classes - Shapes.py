import random

class triangle:

    def __init__(self):
        self.a = random.randint(1,101)
        self.h = random.randint(1,101)

    def printArea(self):
        print(int(self.a * self.h) / 2)


class square:

    def __init__(self):
        self.a = random.randint(1,101)
        self.b = random.randint(1,101)

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