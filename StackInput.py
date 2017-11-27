
from Stacks import *
count = 0
stack = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stackMaxPos = 10


for count in range(0, 10):
    index = input("enter a character")
    push(index, stack)

print(stack)