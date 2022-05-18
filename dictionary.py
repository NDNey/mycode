#!/usr/bin/env python3
deadpool  = {
            'Real Name':'Wade Winston Wilson',
            'Alias':'Deadpool',
            'First Appearance':'New Mutants (Vol. 1) #98 (February, 1991)',
            'Creators':['Fabian Nicieza',' Rob Liefeld'],
            'Base of Operations':'Nomadic'
            }

deadpool['food'] = 'chimichangas'

print("Deadpool's Dictyonary:", deadpool,"\n")
print("Deadpool Dictionary Keys: ",deadpool.keys())

choice = input("\nlook on the dict using a key:\n>")

while(deadpool.get(choice) == None):
    choice = input(f"look on the dict using one of the following keys: {deadpool.keys()}\n>")

print(deadpool.get(choice))
