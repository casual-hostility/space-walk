def myfunc(string):
    listthing = []
    for i in range(len(string)):
        if i % 2 == 0:
            listthing.append(string[i].lower())
        else:
            listthing.append(string[i].upper())

    return ''.join(listthing)