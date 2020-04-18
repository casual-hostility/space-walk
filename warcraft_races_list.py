#making lists

horde_races = ['Tauren', 'Blood Elf', 'Orc', 'Nightborne', 'Undead', 'Highmountain Tauren', 'Goblin', 'Vulpera', 'Maghar Orc', 'Troll', 'Zandalari Troll']
alliance_races = ['Night Elf', 'Draenei', 'Void Elf', 'Human', 'Dwarf', 'Gnome', 'Mechagnome', 'Dark Iron Dwarf', 'Worgen', 'Lightforged Draenei']

print(horde_races, alliance_races) #prints out everything in the list, including brackets. Boo.

print(alliance_races[0]) #prints out element 0 (Night Elf) in the Alliance list

#you can use string formatting onn list elements
print(horde_races[1].upper())

#to return the last item on a list, python uses a special method, calling -1
print(alliance_races[-1])
#-2 returns the second from the end and so on. Counting backwards doesn't start from -0 

message = "My main character is a " + alliance_races[0].lower() + "."
print(message)

#changing, adding and removing list elements
garou = ['Ajay', 'Fray', 'Jack', 'Jessie']
print(garou)

garou[0] = 'R\'lynn' #this replaces the list element at index 0 with the new value
print(garou)
#note: when I run this, R'lynn appears in double quotes instead of single, both inside parenthesis and out

#the append method adds an element to the end of a list
garou.append('Ajay')
print(garou)
#you can start with an empty list and add items with the append method

#note: a fuction is like a group of methods. I think.

#you can add a new element into any position by using the insert method
garou.insert(0, 'Taylor')
print(garou)
#why in the goddamn does R'lynn have double quotes

trees = ['Elm', 'Poplar', 'Cherry']
print(trees)

trees[0] = 'Oak'
print(trees)
#Oak doesn't have double quotes what the fuck?

garou[1] = 'Rlynn'
print(garou)
#it was the damn escaped apostrophe. ok mystery solved.

juice = [] #creates an empty list called 'juice'
juice.append('Apple') #adds Apple to the juice list
print(juice)#prints newly populated juice list
juice.append('Orange')
print(juice)
juice.append('Cranberry')
print(juice)

print(alliance_races[7]) #prints item at index 7 in the alliance_races list

#removing items in a list
garou = ['Jack', 'Ajay', 'Fray'] #i overwrite the list variable 'garou' with new values
print(garou)

del garou[1] #deletes item at index 1 in garou list (Ajay)
print(garou)

garou.reverse() #reverses the actual order of items in a list(reverses 'in-place'), as demonstrated by print function below
print(garou)

print(alliance_races[::-1]) #slicing trick to reverse a list
print(alliance_races)

#removing an item using the pop method to save the value of the removed item
garou.append('Ajay')#just adding Ajay back so my list isn't so short
print(garou)
popped_garou = garou.pop() #created the variable popped_garou to store items popped from the garou list and apparently pops the item in the same statement? 
#no argument in the pop method automatically pops item off the end of list
print(garou)
print(popped_garou)

#copied from the book because I am tired of coming up with lists
motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

alienware = [17,14,15] #made a new list
old_alienware = alienware.pop(1) #pops item from index 1 and stores it in old_alienware variable
print(alienware)
print(old_alienware)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] #made another new list
print(motorcycles)
motorcycles.remove('ducati') #remove method removes an item by name rather than index position
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] #yet another new list
print(motorcycles)
too_expensive = 'ducati' #assigns too_expensive variable to 'ducati' in list
motorcycles.remove(too_expensive) #removes ducati from list by its assigned variable and stores it
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#remove method only removes the first instance  of the value, you have to use a loop to remove more than one instance

cars = ['bmw', 'audi', 'toyota', 'subaru'] #and another new list
cars.sort() #the sort method sorts the list permanently in alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #reverse alphabetical order
print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) #temporarily sorts the list
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) #prints the length of the list

destinations = ['Chichen Itza', 'Galapagos', 'Mars', 'Titan', 'Disney World']
print(destinations)

destinations.sort()
print(destinations)

#doing something after a for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians: #the colon at the end of the for statement tells python to interpret the next line as the start of a loop
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!") #this line is not indented so it will only print once,
#not once for each list item


pizza = ["Alfredo", "Barbeque", "Pineapple"]
for i in pizza:
	print ("I like " + i + ".") 
