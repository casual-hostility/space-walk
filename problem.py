def intergers():
    i=1
    while True:
        yield i
        i = i + 1

def squares():
    for i in intergers():
        yield i * i

def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

print(take(5, squares()))

#so far I have figured out that this is a generator function and that's about it.