nullPointer = -1
class listNode: # record type to store data and pointer
    def __init__(self):
        self.data = ""
        self.pointer = 0

startPointer = 0
currentNodePtr = 0
previousNodePtr = 0
freeListPtr = 0
list = [listNode() for i in range(0,8) ]

def initialiseList():
    global startPointer, freeListPtr, nullPointer
    startPointer = nullPointer # set start pointer
    freeListPtr = 1 # set starting position of free list
    for i in range(1,6): # link all nodes to make free list
        list[i].pointer = i + 1
    list[7].pointer = nullPointer # last node of free list


def InsertNode(newItem):
    global freeListPtr, previousNodePtr, startPointer
    if freeListPtr != nullPointer: # then there is space in the array
        newNodePtr = freeListPtr # take node from free list and store data item
        list[newNodePtr].data = newItem
        freeListPtr = list[freeListPtr].pointer
        # find insertion point
        thisNodePtr = startPointer # start at the beginning of the list
        while thisNodePtr != nullPointer and list[thisNodePtr].data < newItem: # while not end of list
            previousNodePtr = thisNodePtr # remember this node
            # follow pointer to next node
            thisNodePtr = list[thisNodePtr].pointer
        if previousNodePtr == startPointer: # insert new node at start of list
            list[newNodePtr].pointer = startPointer
            startPointer = newNodePtr
        else: # insert new node between previous node and this node
            list[newNodePtr].pointer = list[previousNodePtr].pointer
            list[previousNodePtr].pointer = newNodePtr

def FindNode(dataItem):
    global
    currentNodePtr = startPointer
    while currentNodePtr != nullPointer and list[currentNodePtr].data != dataItem: # not end of list
        # follow the pointer to the next node
        currentNodePtr = list[currentNodePtr].pointer
    return currentNodePtr # returns nullPointer if item not found

def DeleteNode(dataitem):
    global startPointer, freeListPtr, previousNodePtr
    thisNodePTr = startPointer # start at beginning of list
    while thisNodePTr != nullPointer and list[thisNodePTr].data != dataitem: # while not end of list and item not found
        previousNodePtr = thisNodePTr # remember this node
        # follow the pointer to the next node
        thisNodePTr = list[thisNodePTr].pointer
    if thisNodePTr != nullPointer: # node exists in list
        if thisNodePTr == startPointer: # first node to be deleted
            startPointer = list[startPointer].pointer
        else:
            list[previousNodePtr].pointer = list[thisNodePTr].pointer
        list[thisNodePTr].pointer = freeListPtr
        freeListPtr = thisNodePTr

def outputAllNodes():
    currentNodePtr = startPointer # start at beginning of list
    while currentNodePtr != nullPointer: # while not end of list
        print(list[currentNodePtr].data) # follow the pointer to the next node
        currentNodePtr = list[currentNodePtr].pointer

initialiseList()
InsertNode("a")
InsertNode("b")
InsertNode("c")
InsertNode("d")
FindNode("d")
