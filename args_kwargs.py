def myfunc(a,b,c=0,d=0,e=0): #can keep adding arguments OR...
    #returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05
result = myfunc(40,60)
print(result)

def other_func(*args): #adds arguments to a tuple, can now pass in as many arguments as you want
    return sum(args) * 0.05

#can use any keyword you want, doesn't have to be args, just has to have the *

def new_func(**kwargs): #returns back a dictionary instead of a tuple
    if 'fruit' in kwargs:
        print('My favorite fruit is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

result = new_func(fruit='apple', veggie='lettuce')
print(result)

#Now for some fun shit

def funky_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}.".format(args[1],kwargs['food']))
    '''Sooo. It takes the first arguments and puts them in a tuple, then the next arguments in dictionary
    format and formats it out'''
result = funky_func(5,9,80,animal='bats', fruit='banana',food='fries')
print(result)