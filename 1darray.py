# DECLARE ages : ARRAY[0..9] OF INTEGER
# ages = [56,54,64,23,56,23,64,32,12,51]
ages = []
index = 0
count = 0

for index in range(0,10) :
    temp = int(input("Enter age (0-99) "))
    while temp < 0 or temp > 99:
        print("Error.")
        temp = int(input("Enter age (0-99) "))
    ages.append(temp)

for count in range(0,8) :
    for index in range(0,9):
        if ages[index] > ages[index + 1]:
            temp = ages[index]
            ages[index] = ages[index + 1]
            ages[index + 1] = temp
print(ages)
