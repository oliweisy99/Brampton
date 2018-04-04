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
    if freePtr != nullPointer:
        newNodePtr = freePtr
        freePtr = tree[freePtr].leftPointer
        tree[newNodePtr].data = newItem
        tree[newNodePtr].leftPointer = nullPointer
        tree[newNodePtr].rightPointer = nullPointer

        if rootPointer == nullPointer:
            rootPointer = newNodePtr
        else:
            thisNodePtr = rootPointer
            while thisNodePtr != nullPointer:
                previousNodePtr = thisNodePtr
                if tree[thisNodePtr].data > newItem:
                    turnedLeft = True
                    thisNodePtr = tree[thisNodePtr].leftPointer
                else:
                    turnedLeft = False
                    thisNodePtr = tree[thisNodePtr].rightPointer
            if turnedLeft == True:
                tree[previousNodePtr].leftPointer = newNodePtr
            else:
                tree[previousNodePtr].rightPointer = newNodePtr


insertNode("a")
insertNode("z")
insertNode("d")
insertNode("c")
insertNode("b")
insertNode("f")
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




