st = 'Print only the words that start with s in this sentence'
for i in st.split():
    if i.startswith("s"):
        print(i)

#also

for word in st.split():
    if word[0] == 's':
        print(word)

x = []
for i in range(0, 11):
    if i % 2 == 0:
        x.append(i)
    else:
        pass

print(x)


odd = [x for x in range(0, 50) if x%2!=0]
print(odd)

st = 'Print every word in this sentence that has an even number of letters'
even = []
for i in st.split(' '):
    if len(i) % 2 == 0:
        even.append(i)

print(even)


for i in range(1,101): #have to use elif otherwise it still prints the number as well
    if i%3 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

st = 'Create a list of the first letters of every word in this string'
words = st.split()
first_char_list = []
for char in words:
    first_char_list.append(char[0])
print(first_char_list)

st = 'Create a list of the first letters of every word in this string'
words = [word[0] for word in st.split()]
print(words)