# _*_ coding: utf-8 _*_

# Testing

clearing = {
	"n": "forest(impenetrable)",
	"s": "forest(dimly lit, large trees all aroun)",
	"e": "canyon view",
	"w": "forest(tree all directions)"
}

print "*" * 45
print "Welcome to Zork Search Map"
place_at = raw_input("Where are you? > ")
destination = raw_input("Where do you want to go? > ")
print "You're at %s and want to go to %s" % (place_at, destination)
print "*" * 45