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