import random

def __valid(s): #two underscores mean is it is private
    global isValid
    digits = ['0','1','2','3','4','5','6','7','8','9']
    isValid = False
    if len(s) == 4:
        if (s[0] in digits) & (s[1] in digits) & (s[2] in digits) & (s[3] in digits):
            isValid = True
    return isValid

# print(__valid("1234"))

class member():
    def __init__(self):
        Sand = "." # sand is a constant, that is why it doesnt have "self"
        self.__grid = [[Sand for j in range(30)] for i in range(10)]
        self.__mn = ""
        self.__mid = ""
        self.__sp = False
    def setMn(self, mem):
        self.mn = mem
    def setMID(self, id):
        self.mid = id
    def setSP(self,paid):
        self.sp = paid

class junior(member):
    def __init__(self):
        super().__init__()
        self.DOB = ""
    def SetMN(self, memn):
        super().setMn(memn)
    def setMID(self, id):
        super().setMID(id)
    def setSP(self, paid):
        super().setSP(paid)

newMember = junior()
newMember.SetMN = "holida"
newMember.setMID = "cheesE"
print(newMember.setMID)
print(newMember.SetMN)

array = [["E" for i in range(0,7)] for i in range(0,7)] # sets E to all values in 2d array from 8 by 8. so 64 Es.

print(random.randint(0,1000)) # from import random, generates a random integer between 0 and 1000

# a method is a function/procedure starting with def name(self) in a class
# to answer OOP questions, you have to really understand the question and what everything does
# if you do not understand the question, it is going to be really hard for you to answer it
# make sure you understand what the question is asking otherwise it is going to be really hard to answer
# the only and the best way to get good at OOP is to do exam questions on it and make programs with it
# you need to know what the vocab means as well, otherwise you wont know what the question is refering to
# when answering questions, do not rush your coding answers because it is so easy to make silly mistakes.
# when answering the question, plan your answer before writing it down so it makes logical sense to you


'''
encapsulation: combining data and subroutines into a class
class: a type that combines a record with the methods that operate on the properties in the record
attributes: the data items of a class.
methods: the subroutines of a class
object: it is an instance of a class, so if you created a food class, then f = food() is an instance
constructor: a special type of method that is called to create a new object and initialise its attributes
instance: read object

Lets say you have a super class of member and a sub class of junior
junior is declared as:
class junior(member)
    def __init__(self):
    super().__init__() # this takes all the defined attributes of the super class member into junior 
    self.DOB = "" # you can then create an attribute for this subclass that is only used for this subclass. 
    # the junior sub class takes the attributes of the super class member
    
    def setMemberID(self,id):
    super().setMemberID(ID) # this takes the method setMemberID of the superclass and uses it for the junior member
    # you use super().method() to call the method of the super class that you want to use for the subclass
    # you would then pass through the variable you want that gets run through the super class from the sub class

'''
