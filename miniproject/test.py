#!/usr/bin/env python3
from  data import test
from data import heroes
from photos import printPicture

CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[32m'
CGREENEND = '\33[0m'
                        
def getAnswers():       
    total = 0
    for ask in test:
        print("\n",CGREEN + ask["question"] + CGREENEND, "\n")

        for index in range(len(ask["answers"])):
            print(index + 1, ask["answers"][index])

        answer = input("Plese select a number 1 - 4 n\answer: \n> ")

        if answer.isdigit():
            while int(answer) not in range(1, 5):
                print(CRED + "Invalid Input: Plese select a number 1-4 " + CEND)
                answer = input("n\answer: \n> " )
        else:
            while not answer.isdigit():
                print(CRED + "Invalid Input: Plese select a number 1-4 " + CEND)
                answer = input("n\answer: \n> " )
        total += int(answer)

    return total

def getHero():
    answers = getAnswers()
    heroIndex = int(answers/len(test)) - 1
    hero = heroes[heroIndex]

    print("We Know Which Avenger Matches Your Personality Based On The TV Shows You Pick")
    print(CGREEN + hero["alias"] + CGREENEND)
    print(hero["description"])
    printPicture(heroIndex)

def main():
    getHero()
if __name__ == "__main__":
    main()
