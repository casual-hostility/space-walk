mystring = "hello"

mylist = [] #empty list
for letter in mystring: #means 'do this to each item in mystring variable
    mylist.append(letter) #means add each item in the string to the end of mylist

print(mylist)

mylist = [letter for letter in mystring] #'flattened out' for loop

#element for element in 'string' or variable representing a string

newlist = [item for item in "a1h6erf6745"]

print(newlist)

number_list = [x for x in range(0,14)] #adds numbers 0 through 13 to a list
print(number_list)

squared_num = [num**2 for num in range(0, 14)] #added the operator to square each number in the range and put them in the list
print(squared_num)

some_stuff = []
for i in "a list of words":
    some_stuff.append(i)
print(some_stuff)

mylist = [x for x in range(0, 14) if x%2==0] #add number to list if it is even
print(mylist)

celcius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius] #celcius to fahrenheit conversion
print(fahrenheit)
#same as below
farenheit = []
for temp in celcius:
    fahrenheit.append( ((9/5)*temp + 32))

#if, and, else statements in a list comprehension

results = [x if x%2==0 else 'ODD' for x in range(0, 14)]
print(results)

#nested loop UUUUUGH

mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)
#comprehended
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]
