'''
repeated checking of the middle item in an ordered search list and discarding the half of the list
which does not contain the search item
'''

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
# set array of values, values can be changed but must be ordered

target = 8
found = False
startPos = 0
endPos = 9

while found == False and startPos <= endPos: # start position can't be larger than end position
    midPos = (startPos + endPos) // 2  # double // returns integer value... as single / returns float
    if target == number[midPos]:
        found = True
    elif target < number[midPos]:
        endPos = midPos - 1 # if target is lower down than mid, then end position changes
    else:
        startPos = midPos + 1 # if target is higher up than mid, then start position changes

print(found)



