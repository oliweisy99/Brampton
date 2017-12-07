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
ranNumTwo = random.randint(0,10)

def askRep(numRan, team) :
    global count
    count = 0
    while True :
        print(numRan)
        guess = int(input(team + ": guess a number between 1 and 10"))
        if guess == numRan :
            break
        else :
            count = count + 1
    return count

teamOne = askRep(ranNum, first)
print(first, " : ", teamOne)
teamTwo = askRep(ranNumTwo, second)
print(second, " : ", teamTwo)

if teamTwo > teamOne :
    print("")
