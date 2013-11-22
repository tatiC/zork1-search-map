# _*_ coding: utf-8 _*_

# Testing

''' STUFF
Print all possible paths:
for i in clearing:
	print i, clearing[i]
'''	

import os

os.system('clear')

places = ["clearing", "north_of_house", "south_of_house", "west_of_house"]

def check_place(place):
	return places.__contains__(place)
	
def find_passage(place):
	for key, values in zork_map.iteritems():
	    if place in values:
	        print key
	        print directions[zork_map[key].index(place)]	
	
directions = {
0: "n",
1: "ne",
2: "e",
3: "se",
4: "s",
5: "sw",
6: "w",
7: "nw",
}

zork_map = {
	'west of house': ['north of house', 'x', 'door is boarded', 'x', 'south of house', 'x', 'forest 1', 'x'],
    'south of house': ['windows all boarded', 'x', 'behind house', 'x', 'forest 2', 'x', 'west of house', 'x']
    }

find_passage("forest 1")

# print "*" * 45
# print "Welcome to Zork Search Map"
# print "*" * 45
# 
# place_at = raw_input("Where are you? > ")
# while not check_place(place_at):
# 	print "Don't know this place, try again!"
# 	place_at = raw_input("Where are you? > ")
# 
# destination = raw_input("Where do you want to go? > ") 
# while not check_place(destination):	
# 	print "Don't know this place, try again!"
# 	destination = raw_input("Where do you want to go? > ") 