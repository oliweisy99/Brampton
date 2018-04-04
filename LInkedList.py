nullPointer = -1

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
myList[0].pointer = 1 # o points to 1, 1 points to 2 etc.
myList[1].pointer = 2
myList[2].pointer = 3
myList[3].pointer = 4
myList[4].pointer = 5
myList[5].pointer = nullPointer # 5 points to null as it is the end

i = 0
while i != nullPointer: # this links each node to the next node
    print(myList[i].data)
    i = myList[i].pointer

def findNode(target):
    global index, foundPtr
    index = 0
    while index != nullPointer and myList[index].data != target:
        index = myList[index].pointer # moves along linked list to next node using the pointer
    foundPtr = index
    return foundPtr # returns the pointer location of the target letter to be found

print('Result of search for e is: ', findNode("e"))
print('Result of search for l is: ', findNode("l"))
print('Result of serach for p is: ', findNode("p"))

for x in range(0,7):
    print(myList[x].data)







