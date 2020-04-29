nums = [1,2,3,4,5]

for num in nums: #go through each item in the list nums and do something to it
    print(num)

#break keyword will break out of a loop
#continue moves on to the next statement

#loops through the list until it finds 3 then breaks out of the loop/stops
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

#loops through the list until it gets to 3, prints found then keeps going
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

#loop in a loop
for num in nums:
    for letter in 'abc':
        print(num, letter)


for i in range(11):
    print(i)


for letter in 'abc':
    for i in range(1,4):
        print(letter, i)

#incrementing while loop
x = 0
while x < 10: #as long as x is less than 10
    print(x) #print the value of x
    x += 1 #but after you print the value of x, increase the value by 1
 #then start over

 #to keep a loop going forever until it received a condition, use while True