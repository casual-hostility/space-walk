for value in range(1,11):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
#In this example, the range() function starts with the value 2 and then
#adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
#value, 11
print(even_numbers)

squares = []
for value in range(1,11): #assigns each item in the list the value variable in a for loop
    square = value**2 #gets the square root for each item in the list which has been assigned
    #the 'value' variable and assigns the new value to the 'square' variable
    squares.append(square) #adds the assigned value of 'square' to the end of the squares list
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2) #same as above code but without the extra step of assigning the new value to 'square' variable
print(squares)

#finding the minimum, maximum and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

for i in range(1,21):
    print(i)

million = [] #created empty list called 'million'
for i in range(1,1000001):
    million.append(i) #add item in range to list 'million'
#print(million)

odd_numbers = list(range(1,22,2))
print(odd_numbers)

#Weird thing I just noticed. The third argument is still 2 in the even and odd lists, the difference is the starting number
#for the even list I started with 2, the third range argument adds 2 to it therefore printing even numbers in the specified range
#I start with 1 in the odd list and add 2, therefore printing all odd numbers in the range

mult_3 = []
for i in range(3,34): #defines range
    multiple = i*3 #stores the product
    mult_3.append(multiple) #adds product of each item in range to list
print(mult_3)

phrase = "Giraffe Academy"
print(phrase.upper().isupper()) #can use these functions one after another
print(len(phrase)) #prints length of string

print(phrase[0]) #prints char at index 0 in phrase

print(phrase.replace("Giraffe", "Elephant")) #replace giraffe with elephant in the phrase variable

my_num = 5
print(str(5)) #converts int type to string

print(pow(5, 2)) #prints the result of 5 to the power of 2

print(10 % 3) #ten mod 3, prints the remainder of dividing 10 by 3

my_num = -5
print(abs(my_num)) #prints absolute value of my_num variable