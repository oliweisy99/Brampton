
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
# move along the array if the number is smaller and ends the while loop of switching numbers

print(myArray)

# to learn how to write this and understand it:
# write it out, and run your won writen program
# then after you have gone through your array of numbers
# write out the program without looking and test it out yourself
# to revise it, just read the algorithm and do it in your head. if you forgot, try writing it out
# revise it if you forgot, which your going to if you dont read it enough times.
