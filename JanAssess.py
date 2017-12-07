# Number Guessing Game
# Oliver Weisfeld
# 7-12-17

import random

nameArr = ["","","",""]

for i in range(0,4) :
    nameArr[i] = input("enter the name of the team: ")


first = random.choice(nameArr)
second = random.choice(nameArr)
ranNum = random.randint(0,10)


# while True :
  #  count = 0
guess = int(input(first + ": guess a number between 1 and 10"))
