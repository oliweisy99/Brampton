nullPointer = 0

class node:
    def __init__(self):
        self.data = ""
        self.pointer = 0

myList = [node() for index in range(0,9)]
myList[0].data = "h"
myList[1].data = "e"
myList[2].data = "l"
myList[3].data = "p"
myList[4].data = "m"
myList[5].data = "e"
myList[0].pointer = 1
myList[1].pointer = 2
myList[2].pointer = 3
myList[3].pointer = 4
myList[4].pointer = 5
myList[5].pointer = nullPointer

i = 0
while i != nullPointer:
    print(myList[i].data)
    i = myList[i].pointer


