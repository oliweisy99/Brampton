'''
a queue just inputs values, stores them until the space is full, then outputs the first value inputted, then outputs
then value after that which was inputted etc
'''

startPos = 0
endPos = -1
thequeue = []

def enqueue(thequeue, item): # puts an item into the queue
    global endPos # global so that other procedures/functions can use the same end position
    endPos = endPos + 1 # end position is increased by one as one new item has been added to the queue
    thequeue.append(item)  # adds inputted item into the queue
    # thequeue[endPos] = item

def dequeue(thequeue): # takes the first item of the queue
    # DECLARE output : CHAR
    global startPos, endPos
    if startPos == endPos + 1:
        output = "END OF QUEUE" # if the end of queue has been reached as pointers have been moved, then its the end
    else:
        output = thequeue[startPos] # returns the first position of the queue - output
        startPos = startPos + 1 # start position pointer is moved up so the next item will be outputted next time round
    return output

def processqueue(character, thequeue): # display the first item in the queue in lower case
    character = dequeue(thequeue)
    print(character.lower()) # outputs first position of queue from the "De-queue" routine
# setting it to lower case is not necessary, so you can print the first position however you like.

def queueempty(): # tests to see if the queue is empty
    global startPos, endPos, Flag
    if startPos == endPos + 1 :
        Flag = True
    else:
        Flag = False
    return Flag


# new main program
count = 0
while True:
    character = input("enter character")
    enqueue(thequeue, character)
    count = count + 1
    if count >= 5:
        processqueue(character, thequeue)
    if queueempty() == True :
        break