'''
taking in a certain amount of characters then printing them out in reverse order of receiving them using pop and push
'''
stack = []
topPos = -1
basePos = 0

def push(item):
    global topPos
    topPos += 1
    stack.append(item)
    print(stack, topPos)
# push adds item to the stack (array)

def pop():
    global topPos
    output = stack[topPos]
    print("Should output ",output,topPos)
    topPos -= 1
    return output
# pop outputs the reverse of what has been inputted