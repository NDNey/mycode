#!/usr/bin/python3
# Replace RPG starter project with this code when new instructions are live
import requests
from time import sleep
import random

def monster_attack():
    api = "https://v2.jokeapi.dev/joke/Programming,Dark?type=single"
    data = requests.get(api)
    result = data.json()
    return result['joke'] 

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("You see a horrible Monster")
        print(r"""
                        _,.--.
    --..,_           .'`__ o  `;__,
       `'.'.       .'.'`  '---'`  '         
          '.`-...-'.'
            `-...-'
       """)
        print("Why so serious?\n")
        sleep(1)
        print("The monster attacks you!!!\n")
        sleep(1)
        print(monster_attack())
        sleep(10)
        response = input("\nDid the monster make you laugh?[y/n]\n> ")

 

        while response != "y" and response != "n":
            response = input("plese answer [y/n] if you find the joke funny\n> ")

        if response == "y" :
            print('\nThe monster has got you... GAME OVER!')
            break
        else:
            roomsKeys =  list(rooms.keys())
            roomsKeys.remove("Kitchen")
            random_room  =  random.randint(0,len(roomsKeys)-1)
            currentRoom = roomsKeys[random_room]
            print(f"You escape the monster attack this time! The monster sent you to {currentRoom}")
            sleep(2)
