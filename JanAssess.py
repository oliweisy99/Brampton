# Number Guessing Game
# Oliver Weisfeld
# 7-12-17

import random

nameArr = ["","","",""]

for i in range(0,4) :
    nameArr[i] = input("enter the name of the team: ") # put names into array

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


def printCount(ar, f, s, rno, rnt) : # displays guesses made
    global teamOne, teamTwo
    teamOne = ar(rno, f)
    print(f, " had ", teamOne, " guesses")
    teamTwo = ar(rnt, s)
    print(s, " had ", teamTwo, " guesses")


def decision(to, tt, f, s) : # works out and displays the winner
    if tt > to :
        print("team ", f, "wins")
    elif tt < to :
        print("team ", s, " wins")
    else :
        print("draw")

while True : # loop to play until they want to quit
    first = random.choice(nameArr)
    second = random.choice(nameArr)
    ranNum = random.randint(1,10)
    ranNumTwo = random.randint(1,10)
    printCount(askRep, first, second, ranNum, ranNumTwo)
    decision(teamOne, teamTwo, first, second)
    quit = int(input("Do you want to quit? [1 = yes, 0 = no]"))
    if quit == 1 :
        break
    else :
        continue



