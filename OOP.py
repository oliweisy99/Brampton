def __valid(s): #two underscores mean is it is private
    global isValid
    digits = ['0','1','2','3','4','5','6','7','8','9']
    isValid = False
    if len(s) == 4:
        if (s[0] in digits) & (s[1] in digits) & (s[2] in digits) & (s[3] in digits):
            isValid = True
    return isValid

print(__valid("1234"))

# a method is a function/procedure starting with def name(self) in a class
# to answer OOP questions, you have to really understand the question and what everything does
# if you do not understand the question, it is going to be really hard for you to answer it
# the only and the best way to get good at OOP is to do exam questions on it and make programs with it
# you need to know what the vocab means as well, otherwise you wont know what the question is refering to
'''
encapsulation: combining data and subroutines into a class
class: a type that combines a record with the methods that operate on the properties in the record
attributes: the data items of a class
methods: the subroutines of a class
object: an instance of a class, so if you created a food class, then f = food() is an instance
constructor: a special type of method that is called to create a new object and initialise its attributes

'''