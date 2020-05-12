#find out if the word 'dog' is in a string

def dog_check(mystring): #variable can be anything, just needs a placeholder to take an argument
	if 'dog' in mystring.lower(): #forces 'dog' to be lower case so it will match
		return True
	else:
		return False

x = "Did anyone feed the dog yet?"
dog_check(x)

#alternate advanced way to write this function

def dog_check(mystring):
	return 'dog' in mystring.lower() #statement is already a boolean

result = dog_check('is the cat outside')
print(result)

