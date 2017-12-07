# Number Guessing Game
# Oliver Weisfeld
# 7-12-17

import random

nameArr = ["","","",""]

for i in range(0,4) :
    nameArr[i] = input("enter the name of the team: ") # put names into array

first = random.choice(nameArr) # picking random names from array
second = random.choice(nameArr)
ranNum = random.randint(0,10) # picking two random numbers
ranNumTwo = random.randint(0,10)

# def choice(f, s, rn, rnt) :
# f = ...
# s = ...
# rn = ...
# rnt = ...


def askRep(numRan, team) : # getting count for guesses
    global count
    count = 0
    while True :
        guess = int(input(team + ": guess a number between 1 and 10: "))
        if guess == numRan :
            break
        else :
            count = count + 1
    return count


teamOne = askRep(ranNum, first)
print(first, " : ", teamOne)
teamTwo = askRep(ranNumTwo, second)
print(second, " : ", teamTwo) # printing counts for guesses

# def printCount(ar(), f, s, rnt, rn) :
    # global teamone, teamTWo
    # teamOne = ar(rno, f)
    # print ...
    # teamTwo = ar(rnt, s)
    #print...




if teamTwo > teamOne : # deciding who wins
    print("team ", first, " wins")
elif teamTwo < teamOne :
    print("team ", second, " wins")
else :
    print("draw")

# def decision(to, tw, f, s) :
    # if tt > to :
        # pr(..f.)
        #...



# while True :
    # choice(first, second, ranNum, ranNumTwo)
    # printCount(askRep(), first, second, ranNumTwo, ranNum)
    # decision(teamOne, teamTwo, first, second)
    # quit = int(input(("would you like to quit[ 1 = yes, 0, no]"))
        # if quit = 1
            # break
        # else :
            # continue

