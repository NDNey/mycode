#!/usr/bin/env python3
"""
        DIRECTIONS:								
	Copy and paste the dictionary next to your name!								
									
	Return a value from at LEAST FOUR KEY VALUE PAIRS.								
									
	Forge them into a single string! Something like:								
									
	EXAMPLE OUTPUT:								
	Deadpool, aka Wade Wilson, aka Merc with a Mouth, was a member of the X-Force. His most notable power is Accelarated Healing Factor.
"""
invincible = {
        'Real Name':'Mark Grayson',
        'Creator':['Robert Kirkman','Cory Walker'],
        'Team':['Teen Team','The Pact','Guardians of the Globe'],
        'Superpowers':['Superhuman strength','agility','resilience','stamina','flight','extended lifespan','healing factor enhanced'],
        'Father':'Omni Man'
        }

def main():

    for x in invincible:
        if (type(invincible[x]) == str):
            print(invincible[x])

    print("\n========================================\n")

    print(f"{invincible['Real Name']}'s super powers are:  {', '.join(invincible['Superpowers'])}. He is a member of the following teams:  {', '.join(invincible['Superpowers'])}")


main()
