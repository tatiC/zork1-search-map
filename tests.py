# _*_ coding: utf-8 _*_

# Test: 
# Given a place i want to go
# answers where i have to be and the direction i have to take

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

place = "behind house"

for key, values in zork_map.iteritems():
    if place in values:
        print key
        print directions[zork_map[key].index(place)]


