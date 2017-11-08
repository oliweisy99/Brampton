# DECLARE ages : ARRAY[0..9] OF INTEGER
# ages = [56,54,64,23,56,23,64,32,12,51]

index = 0
count = 0

def get_valid_age(): #RETURNS temp
    temp = int(input("Enter age (0-99) "))
    while temp < 0 or temp > 99:
        print("Error.")
        temp = int(input("Enter age (0-99) "))
    return temp

def bubble_sort():
    for count in range(0, 9):
        for index in range(0,9):
            if ages[index] > ages[index + 1]:
                temp = ages[index]
                ages[index] = ages[index + 1]
                ages[index + 1] = temp

def output_array_contents():
    for count in range(0,10):
        print(ages[count])

ages = []
for index in range(0,10) :
    ages.append(get_valid_age())
bubble_sort()
output_array_contents()



