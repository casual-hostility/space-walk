lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Mike", "Max", "Dustin", "Will", "Eleven", "Robin"]
friends.extend(lucky_numbers) #add lucky_numbers list to friends list
friends.append("Lucas")#add object to end of list friends
print(friends)

friends.insert(1, "Joyce") #adds object at index 1
print(friends)

friends.remove("Mike") #remove specific item from list

#friends.clear() #clears list
#friends.pop() #pops item off end of list

print(friends.index("Joyce")) #prints object from list

print(friends.count("Joyce")) #tells you how many times something appears in list

friends.sort() #alphabetizes list

friends2 = friends.copy() #copies a list and saves to new variable