

def push(item, stack):
    global topPos
    topPos = 0
    topPos += 1
    stack[topPos] = item

def pop(topPos):
    global output, stack
    output = stack[topPos]
    topPos -= 1
    return output


