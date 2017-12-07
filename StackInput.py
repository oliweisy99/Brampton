
import Stacks


for count in range(0, 10):
    index = input("enter a character")
    Stacks.push(index)

msg = ""
count = Stacks.topPos
print(count)
while count >= Stacks.basePos:
    msg = msg + Stacks.pop() + ", "
    count -= 1
print(msg)

