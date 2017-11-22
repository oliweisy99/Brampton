number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

target = 8
found = False
startPos = 0
endPos = 9

while found == False and startPos <= endPos:
    midPos = (startPos + endPos) // 2  # double // returns int as single / returns float
    if target == number[midPos]:
        found = True
    elif target < number[midPos]:
        endPos = midPos - 1
    else:
        startPos = midPos + 1

print(found)



