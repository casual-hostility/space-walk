#Original code block
squares = []
for value in range(1,11):
    squares.append(value**2) #same as above code but without the extra step of assigning the new value to 'square' variable
print(squares)

#Comprehended code block, same as above.
squares = [value**2 for value in range(1,11)]
print(squares)