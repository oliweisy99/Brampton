index = 2
count = 1
myArray = [0, 1, 2, 3, 4, 5]

for count in range(0,5):
    item = int(input("what is your input?"))
    myArray[count + 1] = item

for index in range(index, len(myArray)):
    insertItem = myArray[index]
    currentitem = index - 1
    while myArray[currentitem] > insertItem and currentitem > 0:
        myArray[currentitem + 1] = myArray[currentitem]
        currentitem = currentitem - 1
    myArray[currentitem + 1] = insertItem

print(myArray)
