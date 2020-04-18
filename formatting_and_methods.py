first_name = "pj"
last_name = "stroud"

full_name = first_name.title() + " " + last_name.title() #the .title method capitalizes the first letter of each word in a string

print(full_name)

print(full_name.upper()) #the .upper method capitalizes the entire string
print(full_name.lower()) #the .lower method makes all the letters of a string lower case

message = "Hello, " + full_name.title() + "!"
print(message)


#Adding whitespace to strings with tabs and new lines can be done on one line
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#\n is for a new line, \t is to tab

#To remove extra white space from the right end of a string, use rstrip()
favorite_language = 'python '
favorite_editor = 'Geany'
print(favorite_language + favorite_editor) #printing with and without rstrip to demonstrate the difference
print(favorite_language.rstrip() + favorite_editor)

favorite_language = favorite_language.rstrip() #to store the new value back into the original variable

#use lstrip() method to remove space on the left and strip() method to remove both
#idk why you wouldn't just always use strip but whatever
