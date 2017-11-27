stack = []
topPos = -1
basePos = 0

def push(item):
    global topPos
    topPos += 1
    stack.append(item)
    print(stack, topPos)


def pop():
    global topPos
    output = stack[topPos]
    print("Should output ",output,topPos)
    topPos -= 1
    return output

