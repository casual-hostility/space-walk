'''
Pig Latin
*If the word starts with a vowel, add 'ay' to the end
*If the word does not start with a vowel, put the first letter at the end and add 'ay'
*word--> ordway
*apple--> appleay
'''

def pig_latin(word):
    #assign variable to letter at index 0 of a word
    first_letter = word[0] #bc we have to grab that first letter and do something to it

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

result = pig_latin('kaleidoscope')
print(result)

#bc for some reason this IDE won't produce output with just 'return'
# #so I have to assign it to a variable and print it
#able to assign to a variable BECAUSE of the return statement



