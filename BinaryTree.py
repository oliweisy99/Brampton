nullPointer = -1
rootPointer = 0
freePtr = 0

class TreeNode:
    def __init__(self):
        self.data = None
        self.leftPointer = None
        self.rightPointer = None

tree = [TreeNode() for i in range(7)]

def initialiseTree():
    global rootPointer, nullPointer, freePtr, i
    rootPointer = nullPointer
    freePtr = 1
    for i in range(0,6):
        tree[i].leftPointer = i + 1
    tree[6].leftPointer = nullPointer

initialiseTree()

def insertNode(newItem):
    global freePtr, nullPointer, newNodePtr, rootPointer, thisNodePtr, previousNodePtr, turnedLeft
    if freePtr != nullPointer: # if there is space in the array
        newNodePtr = freePtr # take node from free list
        freePtr = tree[freePtr].leftPointer # store data item
        tree[newNodePtr].data = newItem
        tree[newNodePtr].leftPointer = nullPointer # set null pointers
        tree[newNodePtr].rightPointer = nullPointer

        if rootPointer == nullPointer: # check if empty tree
            rootPointer = newNodePtr # insert new node at root
        else: # find insertion point
            thisNodePtr = rootPointer # start at the root of the tree
            while thisNodePtr != nullPointer: # while not a lead node
                previousNodePtr = thisNodePtr # remember this node
                if tree[thisNodePtr].data > newItem:
                    turnedLeft = True # follow left pointer
                    thisNodePtr = tree[thisNodePtr].leftPointer
                else: # follow right pointer
                    turnedLeft = False
                    thisNodePtr = tree[thisNodePtr].rightPointer
            if turnedLeft == True:
                tree[previousNodePtr].leftPointer = newNodePtr
            else:
                tree[previousNodePtr].rightPointer = newNodePtr


insertNode("a")
insertNode("b")
insertNode("f")
insertNode("g")
insertNode("c")
insertNode("d")
print("data:", tree[0].data)
print("leftp:", tree[0].leftPointer)
print("rightp:", tree[0].rightPointer)
print("data:", tree[1].data)
print("leftp:", tree[1].leftPointer)
print("rightp:", tree[1].rightPointer)
print("data:", tree[2].data)
print("leftp:", tree[2].leftPointer)
print("rightp:", tree[2].rightPointer)
print("data:", tree[3].data)
print("leftp:", tree[3].leftPointer)
print("rightp:", tree[3].rightPointer)
print("data:", tree[4].data)
print("leftp:", tree[4].leftPointer)
print("rightp:", tree[4].rightPointer)
print("data:", tree[5].data)
print("leftp:",tree[5].leftPointer)
print("rightp:",tree[5].rightPointer)
print("data:", tree[6].data)
print("leftp:",tree[6].leftPointer)
print("rightp:",tree[6].rightPointer)

'''

-1 a 2
      \ 
    -1 b 3
          \
         5 f 4
        /     \
    -1 c 6  -1 g -1
          \
       -1 d -1
    
'''
def findNode(searchItem):
    global thisNodePtr, nullPointer, rootPointer
    thisNodePtr = rootPointer # start at the root of the tree
    while thisNodePtr != nullPointer and tree[thisNodePtr].data != searchItem: # while a pointer to follow and search item not found
        if tree[thisNodePtr].data > searchItem: # follow left pointer
            thisNodePtr = tree[thisNodePtr].leftPointer
        else: # follow right pointer
            thisNodePtr = tree[thisNodePtr].rightPointer
    return thisNodePtr # returns pointer to node

print(findNode("a")) # returns position in binary tree.
