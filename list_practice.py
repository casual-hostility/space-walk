frogs = []
frogs.append('Leopard')
print(frogs)

frogs.append('Poison Dart')
frogs.append('Bull')
frogs.append('Pacman')

print(frogs)

extinct = frogs.pop()
print(frogs)
print(extinct)

print(sorted(frogs))

print(frogs)

#creates a list called numbers, adds a range of numbers from 1 to 9,999,999 then prints it
numbers =[]
for value in range(1, 1000000):
	numbers.append(value)
print(numbers)

