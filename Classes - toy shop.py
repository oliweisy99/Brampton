class toy:
    def __init__(self):
        # PRIVATE name : STRING
        # PRIVATE id : INTEGER
        # PRIVATE price : REAL
        # PRIVATE minAge : INTEGER

        self.name = None
        self.id = None
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
        print(self.category)
        print(self.console)

class vehicle(toy):
    def __init__(self):
        # PRIVATE type : STRING
        # PRIVATE height : INTEGER
        # PRIVATE length : INTEGER
        # PRIVATE weight : INTEGER

        self.type = None
        self.height = 0
        self.length = 0
        self.weight = 0.0
        super().__init__()

    def display(self):
        print(self.type)
        print(self.height)
        print(self.length)
        print(self.weight)
