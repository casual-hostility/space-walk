def say_hi(): #define function
    print("Hello user")

say_hi() #call function

def say_hello(name): #gives parameter to a function, now have to pass it a name
    print("Hello " + name)

say_hello("PJ") #call function with defined parameter
say_hello("Maleficent")

def say_howdy(name, age): #multiple parameters
    print("Hello " + name + ", you are " + age + " years old")

say_howdy("PJ", "34") #call function with defined parameters
say_howdy("Maleficent", "infinite") #parameters read left to right so just put them in order, they get assigned to variables defined above


def hello_func(): #define a function and leave blank for later, add pass so u wont get an error
    print("Hello Function!")

hello_func()

#keep code 'dry' means dont repeat yourself

def hello_string(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
#an executed function is equal to the RETURN value

print(hello_string('hi'))

#
#
#
def student_info(*args, **kwargs): #will take an arbitrary number of arguments and keyword arguments
    print(args)
    print(kwargs)

courses = ['Math', 'Art'] #arguments
info = {'name': 'PJ', 'age': 34} #keyword arguments

student_info(*courses, **info) #adding the star and double star unpacks the list and tuple