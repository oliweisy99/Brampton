
# from input, this takes your numbers, puts them into an array then re-orders them into ascending value

index = 2
count = 1
myArray = [0, 1, 2, 3, 4, 5]

for count in range(0,len(myArray) - 1):
    item = int(input("what is your input?"))
    myArray[count + 1] = item
# takes input and stores input into array

for index in range(len(myArray)): # to go through each value in the array
    insertItem = myArray[index] # stores value which gets replaced
    currentitem = index - 1
    while myArray[currentitem] > insertItem and currentitem > 0: # going through individual value compared to other values
        myArray[currentitem + 1] = myArray[currentitem]
        currentitem = currentitem - 1
        print(myArray)
    myArray[currentitem + 1] = insertItem
# goes through each number in the array and loops until the number is smaller than the one in front
# switches the number round if the count number is bigger than the number after it in the array
# move along the array if the number is smaller and ends the while loop of switching numberes

print(myArray)
