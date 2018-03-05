class toy:

    def __init__(self):
        # PRIVATE name : STRING
        # PRIVATE id : INTEGER
        # PRIVATE price : REAL
        # PRIVATE minAge : INTEGER

        self.name = ""
        self.id = ""
        self.price = 0.00
        self.minAge = 0

    def display(self):
        print(self.name)
        print(self.id)
        print(self.price)
        print(self.minAge)

class computerGame(toy):

    def __init__(self):
        # PRIVATE category : STRING
        # PRIVATE console : STRING

        self.category = None
        self.console = None
        super().__init__()

    def display(self):
        super().display()
        print(self.category)
        print(self.console)

class vehicle(toy):

    def __init__(self):
        # PRIVATE type : STRING
        # PRIVATE height : INTEGER
        # PRIVATE length : INTEGER
        # PRIVATE weight : INTEGER
        super().__init__()
        self.type = None
        self.height = 0.0
        self.length = 0.0
        self.weight = 0.00

    def display(self):
        super().display()
        print(self.type)
        print(self.height)
        print(self.length)
        print(self.weight)

toy1 = vehicle()
toy1.name = "Red Sports Car"
toy1.id = "RSC13"
toy1.price = 15.00
toy1.minAge = 6
toy1.type = "Car"
toy1.height = 3.3
toy1.length = 12.1
toy1.weight = 0.08
array = [None, None, None]
array[0] = toy1
toy1.display()