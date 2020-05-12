#This is it!! My first on-the-fly program!
#Exercise 1: Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

#Asks for input and stores it in a variable. This runs first.
a = input("Enter your name: ")
b = int(input("Enter your age: "))

def myfunc(a, b): #Defining a function to print the value of stored variables
    print("Hi " + a + ".")
    print("You are " + str(b) + " years old.")

myfunc(a, b) #calls the function with the arguments stored previously

old = b #wanted to store the original value from b to use later

while old:  #my first actual while loop! Wanted to count up to 100 from the input value of b
    old += 1 #adds 1 to the value of old and stores it back in the variable
    if old == 100:
        break #once we reach 100, stop

#Now I have the original value of b and the new value so I can subtract and get the number of years until they're 100.
#Since I don't know what age will be entered I have to just count it up to 100

print("In " + (str(old - b)) + " years you will be 100.")

x = datetime.datetime.now() #gets the current date using the datetime module
new_age = old - b
curr_year = x.year #tells it I only want the year from the datetime module
new_year = curr_year + new_age

print("That will be the year " + (str(new_year)) + ".")
print("How depressing.")