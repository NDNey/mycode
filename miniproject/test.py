#!/usr/bin/env python3
from  data import test
from data import heroes
from photos import printPicture


#colors
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[32m'
CGREENEND = '\33[0m'
      
#Asks and get user's answers      
def getAnswers():       
    total = 0
    for ask in test:
        print("\n",CGREEN + ask["question"] + CGREENEND, "\n")

        for index in range(len(ask["answers"])):
            print(index + 1, ask["answers"][index])

        answer = input("Plese select your answer by it's number 1-4. \nAnswer:\n> ")

        while not answer.isdigit() or int(answer) not in range(1, 5):
            print(CRED + "Invalid Input: Plese select a number 1-4 " + CEND)
            answer = input("\nanswer: \n> " )

        total += int(answer)
        
    return total

#Gets the hero base on user's answer
def getHero():
    answers = getAnswers()
    heroIndex = int(answers/len(test)) - 1
    hero = heroes[heroIndex]

    print("...................................................................................")
    print("\nWe Know Which Avenger Matches Your Personality Based On The TV Shows You Pick\n")
    print("...................................................................................")

    print(CGREEN + hero["alias"] + CGREENEND)
    print(hero["description"])

    printPicture(heroIndex) #Prints hero Ascii Art

#Excecuets the program
def main():
    getHero()

if __name__ == "__main__":
    main()
