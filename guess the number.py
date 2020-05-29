def guess_number():
    my_num = int(47)
    guess = input('Guess a number: ')

    while True:
        if guess < my_num:
            print('Nope, higher')
            pass

        elif guess > my_num:
            print('Nope, lower')
            pass

        elif guess == my_num:
            print('You got it!')
            break


guess_number()