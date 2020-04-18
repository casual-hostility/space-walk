#Working with numbers

#using the range function to generate a series of numbers

for value in range(1,5):
	print(value)

#you can convert the results of range()
#directly into a list using the list() function
numbers = list(range(1,6))
print(numbers)

#starts with the value 2 and then
#adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
#value, 11
even_numbers = list(range(2,11,2))
print(even_numbers)

#a list of the first 10 square numbers
squares = []
for value in range(1,11):
	square = value**2 #this step can be ommitted and each new value appended directly to the list
	squares.append(square)

print(squares)

#or

squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)


#functions specific to lists of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#min(digits)
#0
#max(digits)
#9
#sum(digits)
#45


