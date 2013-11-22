# _*_ coding: utf-8 _*_

# Testing

import os

os.system('clear')

places = ["clearing", "kitchen"]

def check_place(place):
	return places.__contains__(place)
	
# clearing = {
# 	"n": "forest(impenetrable)",
# 	"s": "forest(dimly lit, large trees all aroun)",
# 	"e": "canyon view",
# 	"w": "forest(tree all directions)"
# }
 
print "*" * 45
print "Welcome to Zork Search Map"
print "*" * 45

place_at = raw_input("Where are you? > ")
while not check_place(place_at):
	print "Don't know this place, try again!"
	place_at = raw_input("Where are you? > ")

destination = raw_input("Where do you want to go? > ") 
while not check_place(destination):	
	print "Don't know this place, try again!"
	destination = raw_input("Where do you want to go? > ") 


# if 
# 	print "*" * 45
# 	print "You're at %s and want to go to %s" % (place_at, destination)
# 	print "*" * 45
# else:
# 	print "Ops!!! got an error!"
# 
