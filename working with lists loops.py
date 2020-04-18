#a for loop lets you iterate over each object in a list without changing the code to deal with them individually

magicians = ['alice', 'david', 'carolina'] #define list
for magician in magicians: #define for loop, tells python to pull a name from the list and store it in magician variable
	print(magician) #tells python to print the name that was just stored in the variable magician and repeats line 4 and 5 for each name in the list
#this code tells Python 'for every magician in the list of magicians, print the magician's name'

wolves = ['storm', 'reaper', 'frost'] #doesn't matter what variable you use in the for loop, just have to match
for i in wolves:
	print(i)
#'for every item in the list of wolves, print the item'
