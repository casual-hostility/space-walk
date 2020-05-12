#slicing a list

races = ['Worgen', 'Night Elf', 'Draenei', 'Blood Elf', 'Tauren', 'Troll', 'Human']
print(sorted(races))

for i in races:
	print (i.upper())

print (races[0:3]) #tells python to print objects at index 0 through objects at index 2 and stop at index 3, so the object at 3 won't print

#if you omit the first index, python automatically starts at the first item in the list
print(races[:5]) #starts at the beginning, prints up to object at index 4

print(races[2:]) #starts at index 2 and prints everything after it including the object at index 2

print(races[-3:]) #negative means it will start at the end of the list and print the last 3

#looping through a slice

alienware = ['M15', 'M17', 'M51']
print("here are the types of Alienware Laptops available: ")
for i in alienware[:2]: #tells it to only loop through the first two objects in the list and stop at index 2
	print(i.lower())


#copying a list

my_foods = ['Ice Cream', 'Pizza', 'French Fries', 'Noodles']
friend_foods = my_foods[:] #asks for a slice from my_foods without indexes so it copies the whole list

print("My favorite foods are: ")
print(my_foods[1:3])
print("My friends favorite foods are: ")
print(friend_foods[0:2])

friend_foods.append('Mushrooms') #adding different objects to each list to show they are separate lists
my_foods.append('Soups')

print(my_foods)
print(friend_foods)

#have to copy lists using a slice otherwise Python will simply make one list equal the other 
#e.g. my_foods = friend_foods, it will be the same list
