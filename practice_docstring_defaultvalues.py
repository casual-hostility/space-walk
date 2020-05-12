#adding a docstring adds info when you call help on a function

def name_function():
    """
    DOCSTRING: Information about the function
    Input: no input
    Output: Hello
    """
    print("Hello")

help(name_function)

def say_hello(name):
    print("Hello" + name)

say_hello("PJ") #have to add a parameter if defined in the fucntion above

def say_name(name="NAME"): #set a default if not passed a parameter
    return "hello, " + name

say_name()

#return keyword assigns value to the function, otherwise it just prints and has no value

result = say_name()

print(result)