ten_things = "Painting Drawing Sculpture Dance Performance-Art Architecture"

print "Wait there are not 10 things in that list. Let's fix that." 

stuff = ten_things.split(' ')
more_stuff = ["Printmaking", "Music", "Theatre", "Critique"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding; ", next_one
	stuff.append(next_one)
	print "there are %d items now." % len(stuff)
	
print "There we go:", stuff

print "Let's do something with stuff." 

print stuff[1]
print stuff[-1] #whoa! fancy!
print stuff.pop()
print ' '.join(stuff) # comment
print '#'.join(stuff[3:5]) # comment

