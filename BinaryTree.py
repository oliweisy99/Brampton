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
print(tree[6].leftPointer)