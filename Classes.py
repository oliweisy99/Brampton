# OOP 1
class person:
    #PRIVATE name : STRING
    #PRIVATE age : INTEGER
    #PRIVATE address : STRING

    def display(self):
        print("Person")
        print(self.name)
        print(self.age)
        print(self.address)

    def __init__(self):
        self.name = "Mr X"
        self.age = 15
        self.address = "1 High Street"

class student(person):
    #PRIVATE studentID : STRING

    def display(self):
        print("Student")
        print(self.studentID)
        print(self.name)
        print(self.age)
        print(self.address)

    def __init__(self):
        self.studentID = "S001"
        super().__init__()

class teacher(person):
    # PRIVATE teacherID : STRING
    # PRIVATE specialism : STRING

    def display(self):
        print("Teacher")
        print(self.teacherID)
        print(self.specialism)
        print(self.name)
        print(self.age)
        print(self.address)


    def __init__(self):
        super().__init__()
        self.teacherID = "T001"
        self.specialism = "Computer Science"


a = person()
aa = person()
s = student()
ss = student()
aa.name = "jeffrey"
ss.age = 123
ss.studentID = "S002"

a.display()
aa.display()
ss.display()
s.display()