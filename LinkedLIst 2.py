

class listNode: # record type to store data and pointer
    def __init__(self):
        self.data = ""
        self.pointer = 0


nullPointer = -1
startPointer = 0
freeListPtr = 0
list = [listNode() for i in range(0,9) ]

def initialiseList():
    global startPointer, freeListPtr, nullPointer
    freeListPtr = 0 # set starting position of free list
    for i in range(0,7): # link all nodes to make free list
        list[i].pointer = i + 1
    list[8].pointer = nullPointer # last node of free list

def insetNode(newDataItem):
    global index, freeListPtr
    if freeListPtr != nullPointer:
        index = freeListPtr
        list[index].data = newDataItem
        freeListPtr = list[index].pointer

def findNode(target, startPointer):
    global list
    outputPtr = startPointer
    print(outputPtr)
    while outputPtr != nullPointer and target != list[outputPtr].data:
        outputPtr = list[outputPtr].pointer
    print('EW: ',outputPtr)
    return outputPtr


initialiseList()

insetNode("a")
print(list[0].data)
findNode("a", startPointer)

