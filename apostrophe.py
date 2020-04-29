#The apostrophe can be a problem if you don't use double quotes

message = "One of Python's strengths is its diverse community."
print(message) #No problem

#message = 'One of Python's strengths is its diverse community.' #Syntax error
#print(message) #Yes problem

#I commented out the above lines of code so the good lines will run, don't have debugger installed

message = 'One of Python\'s strengths is its diverse community.' #added escape character
print(message) #Good

#Practice

name = "PJ"
print("Hello " + name + ", would you like to learn some Python today?")

quote = "You've met with a terrible fate, haven't you?"
print(quote.upper())
print(quote.lower())
print(quote.title())

albert = "Albert Einstein once said, \"A person who never made a mistake never tried anything new.\" "
print(albert)

#testing version control with git 4-18-2020