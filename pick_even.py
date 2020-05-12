def myfunc(*args):
    my_list = []
    for i in args:
        if int(i) % 2 == 0:
            my_list.append(i)
    return my_list

result = myfunc(23,9,12,44,71,80)
print(result[0:1])